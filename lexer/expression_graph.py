from lexer.token import Token
from .token_type import TokenType
class Node():
    
    def __init__(self, final_node: bool = False):
        self.connections = dict()
        self.final = final_node

    def __repr__(self) -> str:
        kvps = [f"connections={len(self.connections)}", f"final={self.final}"]
        return f"{type(self).__name__}({', '.join(kvps)})"
    
class ExpressionGraph():
    
    def __init__(self, token_type: TokenType):
        self.root = Node()
        self.token_type = token_type
        self.current_node = self.root
        self.match_length = 0
        self.in_match_state = True

    def reset(self):
        self.current_node = self.root
        self.match_length = 0
        self.in_match_state = True

    def process(self, character):
        if (self.in_match_state and character in self.current_node.connections):
            self.current_node = self.current_node.connections[character]
            self.match_length += 1
        else:
            self.in_match_state = False

    def ended(self):
        return self.current_node.final
        
    def __repr__(self) -> str:
        kvps = [f"{k}={v}" for k, v in vars(self).items()]
        return f"{type(self).__name__}({', '.join(kvps)})"

    
