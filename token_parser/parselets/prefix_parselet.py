from abc import ABC, abstractmethod
from typing import List
from lexer.token import Token

class PrefixParselet(ABC):
    def __init__(self, precedence: int = 0):
        self.precedence = precedence

    @abstractmethod
    def parse(self, token: Token, tokens: List[Token]):
        pass