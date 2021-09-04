from abc import abstractmethod
from lexer.token import Token
from lexer.token import TokenType
from tree_parser.command.base_cmd import BaseCmd
from typing import List
from tree_parser.node import Node
from tree_parser.node_type import NodeType

class BaseParserCmd(BaseCmd):

    @abstractmethod
    def get_type(self): NodeType

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.children = []
        self.root = Node(self.get_type())

    def eat_token(self, *expected_tokens: TokenType) -> Token:
        token = self.tokens.pop(0)
        matches_types = False
        for current_token in expected_tokens:
            matches_types = matches_types or (token.token_type == current_token)
        
        if (not matches_types):
            raise ValueError(f"Expected token of type(s) {expected_tokens} but found {token.token_type} with lexeme \"{token.lexeme}\"")
        print(f"Eating - {token}")
        return token

    def is_next_token(self, token_type: TokenType) -> bool:
        return len(self.tokens) > 0 and self.tokens[0].token_type == token_type