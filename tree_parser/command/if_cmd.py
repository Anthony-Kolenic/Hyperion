from tree_parser.node_type import NodeType
from lexer.token import Token, TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
import tree_parser as tp
from command.command_delegate import CommandDelegate
from tree_parser.node import Node

class IfCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.CONDITIONAL

    def execute(self):
        self.eat_token(TokenType.IF)
        self.eat_token(TokenType.LPAREN)
        self.root.add_child(Node.wrap(CommandDelegate.execute(tp.ExpressionCmd(self.tokens)).root, NodeType.EXPRESSION))
        self.eat_token(TokenType.RPAREN)
        self.eat_token(TokenType.BEGIN)
        self.root.add_child(CommandDelegate.execute(tp.StatementListCmd(self.tokens)).root)
        self.eat_token(TokenType.END)

        while (self.is_next_token(TokenType.ELSE_IF)):
            node = Node(NodeType.CONDITIONAL)
            self.eat_token(TokenType.ELSE_IF)
            self.eat_token(TokenType.LPAREN)
            node.add_child(Node.wrap(CommandDelegate.execute(tp.ExpressionCmd(self.tokens)).root, NodeType.EXPRESSION))
            self.eat_token(TokenType.RPAREN)
            self.eat_token(TokenType.BEGIN)
            node.add_child(CommandDelegate.execute(tp.StatementListCmd(self.tokens)).root)
            self.eat_token(TokenType.END)
            self.root.add_child(node)

        if (self.is_next_token(TokenType.ELSE)):
            node = Node(NodeType.ELSE)
            self.eat_token(TokenType.ELSE)
            self.eat_token(TokenType.BEGIN)
            node.add_child(CommandDelegate.execute(tp.StatementListCmd(self.tokens)).root)
            self.eat_token(TokenType.END)
            self.root.add_child(node)
