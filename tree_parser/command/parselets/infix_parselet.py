from abc import ABC, abstractmethod
from tree_parser.command.base_parser_cmd import BaseParserCmd
from lexer.token import Token
from tree_parser import Node

class InfixParselet(ABC):
    def __init__(self, precedence: int = 0):
        self.precedence = precedence

    @abstractmethod
    def parse(self, left: Node, token: Token, command: BaseParserCmd):
        pass

