from tree_parser.node_type import NodeType
from lexer.token import TokenType, get_variable_types
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.command.expression_cmd import *
from tree_parser.command_delegate import CommandDelegate
from tree_parser.node import Node

""" Method call Command, creates a method call node. 

Method calls consist out of the following and ended semi colon: 
- IDENTIFIER LPARAM EXPRESSION RPARAM
"""
class MethodCallCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.METHOD_CALL

    def execute(self):
        self.root.add_child(Node(NodeType.IDENTIFIER, self.eat_token(TokenType.IDENTIFIER)))
        self.eat_token(TokenType.LPAREN)
        self.root.add_child(Node(NodeType.EXPRESSION, CommandDelegate.execute(ExpressionCmd(self.tokens)).root))
        self.eat_token(TokenType.RPAREN)        