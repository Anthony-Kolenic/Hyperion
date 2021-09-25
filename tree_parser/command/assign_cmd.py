from tree_parser.node_type import NodeType
from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.command.expression_cmd import ExpressionCmd
from command.command_delegate import CommandDelegate
from tree_parser.node import Node

class AssignCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.ASSIGN

    def execute(self):
        self.root.add_child(Node(NodeType.IDENTIFIER, self.eat_token(TokenType.IDENTIFIER)))
        self.eat_token(TokenType.ASSIGN)
        self.root.add_child(CommandDelegate.execute(ExpressionCmd(self.tokens)).root)
        self.eat_token(TokenType.SEMICOLON)