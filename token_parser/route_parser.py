from lexer.token import Token
from lexer.token_type import TokenType
from typing import List
from token_parser.parameter_list_parser import ParameterListParser
from token_parser.statement_list_parser import StatementListParser

from tree_parser.node import Node
from tree_parser.node_type import NodeType
from .base import BaseParser, eat_token


class RouteParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        node = Node(NodeType.METHOD)
        eat_token(tokens, TokenType.ROUTE)
        node.add_child(Node(NodeType.IDENTIFIER, eat_token(tokens, TokenType.IDENTIFIER)))
        eat_token(tokens, TokenType.LPAREN)
        node.add_child(ParameterListParser.parse(tokens))
        eat_token(tokens, TokenType.RPAREN)
        eat_token(tokens, TokenType.COLON)
        node.add_child(Node(NodeType.RETURN_TYPE, eat_token(tokens, TokenType.INT, TokenType.DBL, TokenType.STRING, TokenType.CHAR, TokenType.BOOL, TokenType.VOID)))
        eat_token(tokens, TokenType.BEGIN)
        node.add_child(StatementListParser.parse(tokens))
        eat_token(tokens, TokenType.END)
        return node
    
    