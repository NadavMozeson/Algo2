from Builder.GraphCreator import *
from Builder.GraphBuilder import *
from Builder.GraphCreatorApp import GraphCreatorApp, UserInput
from Builder.AlgorithmRules import *
from Builder.Algorithms import *
import time


def build_graph(option, nodes_amount=5, is_directed=False, has_weights=False, flow=False, node_class=Node,
                has_cycle=True):
    if option == 'random':
        return generate_random_graph(num_of_nodes=nodes_amount, is_directed=is_directed, has_weight=has_weights,
                                     flow=flow, NodeClass=node_class, has_cycle=has_cycle)
    elif option == 'draw':
        drawApp = GraphBuilderApp(directed=is_directed, weighted=has_weights, flow=flow, node_class=node_class)
        drawApp.run()
        return drawApp.graph


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphCreatorApp(root)
    root.mainloop()
    user_input: UserInput = app.return_result()
    print(user_input)
    algo_roles: AlgoRule = ALGORITHMS.get_algo_rule(algorithm=user_input.algorithm)

    graph = None

    if user_input.loaded_filename:
        graph = Graph.load(user_input.loaded_filename)
    else:
        graph = build_graph(option=user_input.generation_method, nodes_amount=user_input.nodes_amount,
                            is_directed=user_input.is_directed, has_weights=user_input.has_weight,
                            node_class=algo_roles.node_class, flow=algo_roles.flow, has_cycle=algo_roles.circular)
    if user_input.save:
        graph.save(user_input.filename)

    graph.print()
    graph.display()

    ALGORITHMS.run_algorithm(graph=graph, algorithm=user_input.algorithm)
