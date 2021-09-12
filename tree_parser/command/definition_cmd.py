from tree_parser.node_type import NodeType
from lexer.token import TokenType, get_variable_types
from tree_parser.command.base_parser_cmd import BaseParserCmd
from command.command_delegate import CommandDelegate
from tree_parser.node import Node

class DefinitionCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.DEFINITION

    def execute(self):
        self.eat_token(TokenType.DEF)
        self.root.add_child(Node(NodeType.IDENTIFIER, self.eat_token(TokenType.IDENTIFIER)))
        self.eat_token(TokenType.COLON)
        self.root.add_child(Node(NodeType.TYPE, self.eat_token(*get_variable_types())))
        if (self.is_next_token(TokenType.SEMICOLON)):
            self.eat_token(TokenType.SEMICOLON)
        elif (self.is_next_token(TokenType.EQUAL)):
            self.eat_token(TokenType.EQUAL)
            self.root.add_child(Node(NodeType.EXPRESSION, self.eat_token()))
        else:
            raise ValueError(f"Expected expression but found {self.tokens[0].token_type} with lexeme \"{self.tokens[0].lexeme}\"")