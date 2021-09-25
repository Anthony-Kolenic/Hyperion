from tree_parser.node_type import NodeType
from lexer.token import Token
from tree_parser.node_type import NodeType

class Node():
    uuid = 0

    def __init__(self, node_type: NodeType, token: Token = None):
        self.token = token
        self.node_type = node_type
        self.id = Node.uuid
        self.children = []
        Node.uuid += 1
    
    def add_child(self, node):
        self.children.append(node)

    def get_child_by_type(self, node_type: NodeType):
        child = None
        for current_child in self.children:
            if (current_child.node_type == node_type):
                child = current_child
                break
        return child

    @staticmethod
    def wrap(node, wrapper_type: NodeType, token: Token = None):
        new_node = Node(wrapper_type, token)
        new_node.children.append(node)
        return new_node

    def __repr__(self) -> str:
        kvps = [f"{k}={v}" for k, v in vars(self).items()]
        return f"{type(self).__name__}({', '.join(kvps)})"

