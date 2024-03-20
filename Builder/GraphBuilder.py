import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
from Builder.GraphCreator import *
import math

class GraphBuilderApp:
    """
    An application that enables to build and create a graph using GUI
    """
    def __init__(self, directed=True, weighted=False, node_class=Node):
        self.directed = directed
        self.weighted = weighted
        self.root = tk.Tk()
        self.root.title("Graph Builder")

        self.graph = Graph(directed=directed, weighted=weighted, NodeClass=node_class)
        self.selected_node = None

        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.add_node)
        self.canvas.bind("<Button-3>", self.add_line)

        self.nodes = {}

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_node(self, event):
        x, y = event.x, event.y
        label = simpledialog.askstring("Enter label", "Enter the label for the node:")
        self.nodes[label] = (x, y)
        self.graph.add_node(label)
        self.canvas.create_oval(x - 40, y - 40, x + 40, y + 40, fill="#1f78b4", outline="")
        self.canvas.create_text(x, y, text=str(label), fill="black", font=("Helvetica", 30, "bold"))

    def add_line(self, event):
        x, y = event.x, event.y
        for label, (nx, ny) in self.nodes.items():
            if (x - nx) ** 2 + (y - ny) ** 2 <= 1600:  # Reduce the radius to 40 pixels (20 * 20)
                if self.selected_node:
                    start_x, start_y = self.nodes[self.selected_node][0], self.nodes[self.selected_node][1]
                    end_x, end_y = x, y
                    node_radius = 40
                    angle = math.atan2(end_y - start_y, end_x - start_x)
                    start_x = start_x + node_radius * math.cos(angle)
                    start_y = start_y + node_radius * math.sin(angle)

                    if not self.graph.has_line(self.selected_node, label):
                        if self.weighted:
                            weight = simpledialog.askinteger("Enter weight", "Enter the weight for the line:")
                            if weight is not None:
                                self.graph.add_line(self.selected_node, label, weight)
                                if self.directed:
                                    self.canvas.create_line(start_x, start_y, end_x, end_y,
                                                            fill="black", width=3, arrow=tk.LAST, arrowshape=(15, 20, 8))
                                else:
                                    self.canvas.create_line(start_x, start_y, end_x, end_y,
                                                            fill="black", width=3)
                                mid_x = (start_x + end_x) / 2 - 10
                                mid_y = (start_y + end_y) / 2 - 10
                                self.canvas.create_text(mid_x, mid_y, text=str(weight), fill="black", font=("Helvetica", 15, "bold"))
                        else:
                            self.graph.add_line(self.selected_node, label)
                            self.canvas.create_line(start_x, start_y, end_x, end_y,
                                                    fill="black", width=3, arrow=tk.LAST, arrowshape=(15, 20, 8))
                    else:
                        messagebox.showwarning("Line exists", "Line already exists in the graph.")
                    self.selected_node = None
                    return
                else:
                    self.selected_node = label
                    return
        messagebox.showwarning("Warning", "Please click near a node to create an edge.")

    def on_closing(self):
        self.root.destroy()

    def get_graph(self):
        return self.graph

    def run(self):
        self.root.mainloop()
