import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from os.path import dirname, realpath, basename

class GraphCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Creator")

        self.current_section = 1

        self.algorithm_var = tk.StringVar()
        self.nodes_var = tk.StringVar()
        self.directed_var = tk.BooleanVar()
        self.weight_var = tk.BooleanVar()
        self.save_var = tk.BooleanVar()
        self.filename = ""
        self.loaded_filename = ""

        self.create_section1()

        self.result = {
            'HAS_WEIGHT': False,
            'IS_DIRECTED': False,
            'NODE_AMOUNT': 0,
            'OPTION': '',
            'ALGORITHM': '',
            'SAVE': False,
            'FILE_NAME': '',
            'LOAD_NAME': ''
        }

    def create_section1(self):
        self.algorithm_label = tk.Label(self.root, text="Algorithm Picker:")
        self.algorithm_label.pack()

        self.algorithm_dropdown = ttk.Combobox(self.root, textvariable=self.algorithm_var, values=[
            "BFS", "DFS", "Topologic Sort", "Kosaraju-Sharir", "Kruskal", "Prim", "Dijkstra",
            "Bellman-Ford", "Floyd-Warshall", "DAG Shortest Path"
        ])
        self.algorithm_dropdown.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.move_to_section2)
        self.next_button.pack()

    def load_graph(self):
        self.loaded_filename = basename(filedialog.askopenfilename(title="Select Graph File", initialdir=dirname(dirname(realpath(__file__)))))
        if self.loaded_filename:
            messagebox.showinfo("Info", f"Graph loaded from file: {self.loaded_filename}")
            self.submit_data()

    def move_to_section2(self):
        if self.algorithm_var.get() == "":
            tk.messagebox.showwarning("Warning", "Please select an algorithm.")
            return

        self.algorithm_label.pack_forget()
        self.algorithm_dropdown.pack_forget()
        self.next_button.pack_forget()

        self.create_section2()
        self.current_section = 2

    def create_section2(self):
        self.graph_creator_label = tk.Label(self.root, text="Graph Creator:")
        self.graph_creator_label.pack()

        self.load_button = tk.Button(self.root, text="Load Graph", command=self.load_graph)
        self.load_button.pack()

        self.generation_label = tk.Label(self.root, text="Choose Generation Method:")
        self.generation_label.pack()

        self.method_var = tk.StringVar(value="random")  # Set default to "random"

        self.random_toggle = tk.Radiobutton(self.root, text="Random", variable=self.method_var, value="random",
                                            command=self.show_random_fields)
        self.random_toggle.pack()

        self.draw_toggle = tk.Radiobutton(self.root, text="Draw", variable=self.method_var, value="draw",
                                          command=self.show_draw_fields)
        self.draw_toggle.pack()

        self.show_random_fields()

        self.save_checkbox = tk.Checkbutton(self.root, text="Save Graph", variable=self.save_var,
                                            command=self.show_save_entry)
        self.save_checkbox.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_data)
        self.submit_button.pack()

    def show_random_fields(self):
        self.remove_draw_fields()

        self.nodes_label = tk.Label(self.root, text="How many nodes does the graph have?")
        self.nodes_label.pack()

        self.nodes_entry = tk.Entry(self.root, textvariable=self.nodes_var)
        self.nodes_entry.pack()

        self.directed_checkbox = tk.Checkbutton(self.root, text="Is the graph directed?", variable=self.directed_var)
        self.directed_checkbox.pack()

        self.weight_checkbox = tk.Checkbutton(self.root, text="Does the graph have weight?", variable=self.weight_var)
        self.weight_checkbox.pack()

    def show_draw_fields(self):
        self.remove_random_fields()

        self.directed_checkbox = tk.Checkbutton(self.root, text="Is the graph directed?", variable=self.directed_var)
        self.directed_checkbox.pack()

        self.weight_checkbox = tk.Checkbutton(self.root, text="Does the graph have weight?", variable=self.weight_var)
        self.weight_checkbox.pack()

    def show_save_entry(self):
        if self.save_var.get():
            self.filename_entry_label = tk.Label(self.root, text="Enter File Name:")
            self.filename_entry_label.pack()

            self.filename_entry = tk.Entry(self.root)
            self.filename_entry.pack()
        else:
            if hasattr(self, 'filename_entry_label'):
                self.filename_entry_label.pack_forget()
                self.filename_entry.pack_forget()

    def remove_random_fields(self):
        if hasattr(self, 'nodes_label'):
            self.nodes_label.pack_forget()
            self.nodes_entry.pack_forget()
            self.directed_checkbox.pack_forget()
            self.weight_checkbox.pack_forget()

    def remove_draw_fields(self):
        if hasattr(self, 'directed_checkbox'):
            self.directed_checkbox.pack_forget()
            self.weight_checkbox.pack_forget()

    def submit_data(self):
        algorithm = self.algorithm_var.get()
        if algorithm == "":
            tk.messagebox.showwarning("Warning", "Please select an algorithm.")
            return

        generation_method = self.method_var.get()
        if generation_method == "":
            tk.messagebox.showwarning("Warning", "Please select a generation method.")
            return

        save = self.save_var.get()
        filename = self.filename_entry.get() if save else ""

        if self.current_section == 2:
            nodes = self.nodes_var.get()
            directed = self.directed_var.get()
            weight = self.weight_var.get()
            self.result['OPTION'] = generation_method
            self.result['ALGORITHM'] = algorithm
            self.result['NODE_AMOUNT'] = (int(nodes) if nodes != '' else 0)
            self.result['IS_DIRECTED'] = directed
            self.result['HAS_WEIGHT'] = weight
            self.result['SAVE'] = save
            self.result['FILE_NAME'] = filename
            self.result['LOAD_NAME'] = self.loaded_filename

        self.root.quit()

    def return_result(self):
        return self.result
