from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.node import Node
from tree_parser.node_type import NodeType

class StatementListCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.STATEMENT_LIST

    def execute(self):
        while (len(self.tokens) > 0 and not self.is_next_token(TokenType.END)):
            self.eat_token(TokenType.RETURN)
            self.eat_token(TokenType.INT_LITERAL)
            self.eat_token(TokenType.SEMICOLON)


