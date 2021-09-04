from lexer.token import Token
from lexer.token import TokenType
from .base_cmd import BaseCmd
from typing import Deque, List
from tree_parser.node import Node

class RouteCmd(BaseCmd):

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.root = Node(Token(TokenType.ROUTE, "")) # TODO: Add tree node types

    def execute(self):
        self.root.add_child(self.eat_token(self.tokens, TokenType.ROUTE))
        self.root.add_child(self.eat_token(self.tokens, TokenType.IDENTIFIER))
        self.root.add_child(self.eat_token(self.tokens, TokenType.LPAREN))
        self.root.add_child(self.eat_token(self.tokens, TokenType.VOID))
        self.root.add_child(self.eat_token(self.tokens, TokenType.RPAREN))
        self.root.add_child(self.eat_token(self.tokens, TokenType.COLON))
        self.root.add_child(self.eat_token(self.tokens, TokenType.INT))
        self.root.add_child(self.eat_token(self.tokens, TokenType.BEGIN))
        print(self.root)
        # route = self.eat_token(self.tokens, TokenType.INT)
        # route = self.eat_token(self.tokens, TokenType.END)