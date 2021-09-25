from .prefix_parselet import PrefixParselet
from lexer.token import Token
from tree_parser.node import Node, NodeType
from tree_parser.command.base_parser_cmd import BaseParserCmd

class IdentifierParselet(PrefixParselet):
    def parse(self, token: Token, command: BaseParserCmd):
        return Node(NodeType.IDENTIFIER, token)