from abc import ABC, abstractmethod
from tree_parser.command.base_parser_cmd import BaseParserCmd
from lexer.token import Token

class PrefixParselet(ABC):
    def __init__(self, precedence: int = 0):
        self.precedence = precedence

    @abstractmethod
    def parse(self, token: Token, command: BaseParserCmd):
        pass