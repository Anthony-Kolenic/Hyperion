from lexer.token import Token
from lexer.token import TokenType
from .base_cmd import BaseCmd
from typing import Deque, List

class RouteCmd(BaseCmd):

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        # self.node = Node()

    def execute(self):
        route = self.eat_token(self.tokens, TokenType.ROUTE)
        route = self.eat_token(self.tokens, TokenType.IDENTIFIER)
        route = self.eat_token(self.tokens, TokenType.LPAREN)
        route = self.eat_token(self.tokens, TokenType.VOID)
        route = self.eat_token(self.tokens, TokenType.RPAREN)
        route = self.eat_token(self.tokens, TokenType.COLON)
        route = self.eat_token(self.tokens, TokenType.INT)
        route = self.eat_token(self.tokens, TokenType.BEGIN)
        # route = self.eat_token(self.tokens, TokenType.INT)
        # route = self.eat_token(self.tokens, TokenType.END)