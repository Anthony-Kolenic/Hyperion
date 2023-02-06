from lexer.token import Token
from lexer.token_type import TokenType
from typing import Callable, Dict, List

from token_parser.route_parser import RouteParser
from tree_parser.node import Node
from tree_parser.node_type import NodeType
from .base import BaseParser

class FileParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        processors: Dict[TokenType, Callable] = {
            TokenType.ROUTE: RouteParser
        }
        root = Node(NodeType.ROOT)
        while tokens:
            token = tokens[0]
            if token.token_type not in processors:
                raise Exception(f"Unexpected token \"{token.lexeme}\", expected function definition or import")
            root.add_child(processors[token.token_type].parse(tokens))
        return root