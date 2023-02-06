from typing import List
from .prefix_parselet import PrefixParselet
from lexer.token import Token
from tree_parser.node import Node, NodeType

class LiteralParselet(PrefixParselet):
    def parse(self, token: Token, _: List[Token]):
        return Node(NodeType.TERM, token)