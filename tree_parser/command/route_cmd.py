from tree_parser.node_type import NodeType
from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.command.parameter_list_cmd import ParameterListCmd
from tree_parser.command.statement_list_cmd import StatementListCmd
from tree_parser.command_delegate import CommandDelegate
from tree_parser.node import Node

class RouteCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.METHOD

    def execute(self):
        self.eat_token(TokenType.ROUTE)
        self.root.add_child(Node(NodeType.IDENTIFIER, self.eat_token(TokenType.IDENTIFIER)))
        self.eat_token(TokenType.LPAREN)
        self.root.add_child(CommandDelegate.execute(ParameterListCmd(self.tokens)).root)
        self.eat_token(TokenType.RPAREN)
        self.eat_token( TokenType.COLON)
        self.root.add_child(Node(NodeType.RETURN_TYPE, self.eat_token(TokenType.INT)))
        self.eat_token(TokenType.BEGIN)
        self.root.add_child(CommandDelegate.execute(StatementListCmd(self.tokens)).root)
        self.eat_token(TokenType.END)
        # route = self.eat_token(self.tokens, TokenType.INT)
        # route = self.eat_token(self.tokens, TokenType.END)