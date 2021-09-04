from lexer.token import Token

class Node():
    uuid = 0

    def __init__(self, token: Token):
        self.token = token
        self.id = Node.uuid
        self.children = []
        Node.uuid += 1

    
    def add_child(self, node):
        self.children.append(node)

    def __repr__(self) -> str:
        kvps = [f"{k}={v}" for k, v in vars(self).items()]
        return f"{type(self).__name__}({', '.join(kvps)})"

