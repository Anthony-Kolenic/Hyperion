from typing import List
import token_parser
from .prefix_parselet import PrefixParselet
from lexer.token import Token
from tree_parser import Node, NodeType

class PrefixOperatorParselet(PrefixParselet):
    def parse(self, token: Token, tokens: List[Token]):
        node = Node(NodeType.UNARY_OPERATION, token)
        node.add_child(token_parser.ExpressionParser.parse(tokens, self.precedence))
        return node
    
