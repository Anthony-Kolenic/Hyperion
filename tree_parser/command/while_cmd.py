from tree_parser.node_type import NodeType
from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
import tree_parser as tp
from command.command_delegate import CommandDelegate

class WhileCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.WHILE_LOOP

    def execute(self):
        self.eat_token(TokenType.WHILE)
        self.eat_token(TokenType.LPAREN)
        self.root.add_child(CommandDelegate.execute(tp.ExpressionCmd(self.tokens)).root)
        self.eat_token(TokenType.RPAREN)
        self.eat_token(TokenType.BEGIN)
        self.root.add_child(CommandDelegate.execute(tp.StatementListCmd(self.tokens)).root)
        self.eat_token(TokenType.END)