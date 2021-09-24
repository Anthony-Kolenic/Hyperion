from command.base_cmd import BaseCmd
from tree_parser import Node
import graphviz

class TreeOutputCmd(BaseCmd):
    def __init__(self, root):
        self.root = root
        self.id = 0
        self.graph = graphviz.Digraph(comment='AST')

    def execute(self):
        self.append_to_graph(self.root, self.graph)

    def append_to_graph(self, node: Node, graph):
        print(node.node_type, node.token)
        if node.token is not None:
            graph.node(str(node.id), f'{node.node_type} ({node.token.token_type}: {node.token.lexeme})')
        else:
            graph.node(str(node.id), f'{node.node_type}')
        for current_node in node.children:
            graph.edge(str(node.id), str(current_node.id))
            self.append_to_graph(current_node, graph)

    def result(self):
        return self.graph.source
