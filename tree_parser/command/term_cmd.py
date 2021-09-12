from tree_parser.node_type import NodeType
from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.node import Node

""" Terms Command, deals with an terms where terms are tokens that equate to tangible values. 

Terms's consist out of the following and ended semi colon: 
- ID
- INT LITERAL
- STRING LITERAL
- CHAR LITERAL
- DOUBLE LITERAL
"""
class TermCmd(BaseParserCmd):
    valid_types = [TokenType.IDENTIFIER, TokenType.INT_LITERAL, TokenType.STR_LITERAL, TokenType.CHAR_LITERAL, TokenType.DBL_LITERAL]

    def get_type(self):
        return NodeType.TERM

    def execute(self):
        if (TermCmd.is_term(self.tokens)):
            self.root.add_child(Node(NodeType.TERM, self.eat_token(*TermCmd.valid_types)))
        else:
            raise ValueError(f"Expected expression but found {self.tokens[0].token_type} with lexeme \"{self.tokens[0].lexeme}\"")

    @staticmethod
    def is_term(tokens):
        return len(tokens) > 1 and tokens[1].token_type == TokenType.SEMICOLON and tokens[0].token_type in TermCmd.valid_types
        