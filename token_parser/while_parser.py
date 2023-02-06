from lexer.token import Token
from lexer.token_type import TokenType
from typing import List
import token_parser

from tree_parser.node import Node
from tree_parser.node_type import NodeType
from .base import BaseParser, are_next_tokens, eat_token
from lexer.token import TokenType

class WhileParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        root = Node(NodeType.WHILE_LOOP)
        eat_token(tokens, TokenType.WHILE)
        eat_token(tokens, TokenType.LPAREN)
        root.add_child(token_parser.ExpressionParser.parse(tokens))
        eat_token(tokens, TokenType.RPAREN)
        eat_token(tokens, TokenType.BEGIN)
        root.add_child(token_parser.StatementListParser.parse(tokens))
        eat_token(tokens, TokenType.END)

        return root
    
    