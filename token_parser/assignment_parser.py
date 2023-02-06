from lexer.token import Token
from lexer.token_type import TokenType
from typing import List
import token_parser

from tree_parser.node import Node
from tree_parser.node_type import NodeType
from .base import BaseParser, eat_token
from lexer.token import TokenType

class AssignmentParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        root = Node(NodeType.ASSIGN)
        root.add_child(Node(NodeType.IDENTIFIER, eat_token(tokens, TokenType.IDENTIFIER)))
        eat_token(tokens, TokenType.ASSIGN)
        root.add_child(token_parser.ExpressionParser.parse(tokens))
        return root
    
    