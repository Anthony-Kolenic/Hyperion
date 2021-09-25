from .prefix_parselet import PrefixParselet
from tree_parser.command.base_parser_cmd import BaseParserCmd
from lexer.token import Token, TokenType
from command import CommandDelegate
import tree_parser as tp

class GroupParselet(PrefixParselet):
    def parse(self, token: Token, command: BaseParserCmd):
        node = CommandDelegate.execute(tp.ExpressionCmd(command.tokens)).root
        command.eat_token(TokenType.RPAREN)
        return node