from abc import ABC, abstractmethod
from lexer.token_type import TokenType
from lexer.token import Token
from typing import List

class BaseCmd(ABC):
    
    @abstractmethod
    def execute(self):
        pass

    def eat_token(self, tokens:List[Token], expected_token: TokenType):
        token = tokens.pop(0)
        if (token.token_type != expected_token):
            raise ValueError(f"Expected token of type {expected_token} but found {token.token_type} with lexeme \"{token.lexeme}\"")
        print(f"Eating - {token}")
        return token