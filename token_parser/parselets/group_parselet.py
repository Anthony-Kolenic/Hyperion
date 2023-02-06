from typing import List

import token_parser
from token_parser.base import eat_token
from .prefix_parselet import PrefixParselet
from lexer.token import Token, TokenType

class GroupParselet(PrefixParselet):
    def parse(self, token: Token, tokens: List[Token]):
        node = token_parser.ExpressionParser.parse(tokens)
        eat_token(tokens, TokenType.RPAREN)
        return node