from lexer.token import Token
from lexer.token_type import TokenType
from typing import List
from token_parser.expression_parser import ExpressionParser

from tree_parser.node import Node
from tree_parser.node_type import NodeType
from .base import BaseParser, eat_token
from lexer.token import TokenType

class ReturnParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        root = Node(NodeType.RETURN)
        eat_token(tokens, TokenType.RETURN)
        # Add Child as expression
        root.add_child(ExpressionParser.parse(tokens))
        return root
    
    