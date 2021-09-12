from tree_parser.command.method_call_cmd import MethodCallCmd
from tree_parser.node_type import NodeType
from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.command.term_cmd import TermCmd
from tree_parser.command.unary_operation_cmd import UnaryOperationCmd
from command.command_delegate import CommandDelegate
from tree_parser.node import Node

""" Expression Command, deals with an expression. 

Expression's consist out of the following and ended semi colon: 
- TERM
- NOT EXPRESSION
- ID LPARAM EXPRESSION RPARAM
- LPAREN EXPRESSION RPARAM
- EXPRESSION
- EXPRESSION ADD EXPRESSION
- EXPRESSION SUB EXPRESSION
- EXPRESSION MUL EXPRESSION
- EXPRESSION DIV EXPRESSION
- EXPRESSION MOD EXPRESSION
- EXPRESSION AND EXPRESSION
- EXPRESSION OR EXPRESSION
- EXPRESSION XOR EXPRESSION
- EXPRESSION GT EXPRESSION
- EXPRESSION ST EXPRESSION
- EXPRESSION GTE EXPRESSION
- EXPRESSION STE EXPRESSION
- EXPRESSION EQUALITY EXPRESSION
- EXPRESSION INEQUALITY EXPRESSION
"""
class ExpressionCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.EXPRESSION

    def execute(self):
        if (TermCmd.is_term(self.tokens)):
            self.root.add_child(Node(NodeType.TERM, CommandDelegate.execute(TermCmd(self.tokens)).root))
        elif UnaryOperationCmd.is_unary_operation(self.tokens):
            self.root.add_child(Node(NodeType.UNARY_OPERATION, CommandDelegate.execute(UnaryOperationCmd(self.tokens)).root))
        elif self.is_next_token(TokenType.IDENTIFIER, TokenType.LPAREN):
            self.root.add_child(Node(NodeType.METHOD_CALL, CommandDelegate.execute(MethodCallCmd(self.tokens)).root))
        elif self.is_next_token(TokenType.LPAREN):
            self.eat_token(TokenType.LPAREN)
            self.root.add_child(Node(NodeType.EXPRESSION, CommandDelegate.execute(ExpressionCmd(self.tokens)).root))
            self.eat_token(TokenType.RPAREN)
        else:
            raise ValueError(f"Expected expression but found {self.tokens[0].token_type} with lexeme \"{self.tokens[0].lexeme}\"")