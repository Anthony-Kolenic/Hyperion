from typing import List

import token_parser

from .prefix_parselet import PrefixParselet
from lexer.token import Token
import tree_parser as tp
from tree_parser import Node, NodeType

class InfixOperatorParselet(PrefixParselet):

    def parse(self, left: Node, token: Token, tokens: List[Token]):
        node = Node(NodeType.BINARY_OPERATION, token)
        node.add_child(left)
        node.add_child(token_parser.ExpressionParser.parse(tokens, self.precedence))
        return node
    
