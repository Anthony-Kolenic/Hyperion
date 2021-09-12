from tree_parser.node_type import NodeType
from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.command.expression_cmd import *
from command.command_delegate import CommandDelegate
from tree_parser.node import Node

""" Method call Command, creates a method call node. 

Method calls consist out of the following and ended semi colon: 
- OPERATION EXPRESSION
"""
class UnaryOperationCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.UNARY_OPERATION

    def execute(self):
        if (self.is_next_token(TokenType.NOT)):
            self.root.add_child(Node(NodeType.OPERATION, self.eat_token(TokenType.NOT)))
            self.root.add_child(Node(NodeType.EXPRESSION, CommandDelegate.execute(ExpressionCmd(self.tokens)).root))
    
    @staticmethod
    def is_unary_operation(tokens):
        return len(tokens) > 0 and tokens[0].token_type == TokenType.NOT