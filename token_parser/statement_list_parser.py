from lexer.token import Token
from lexer.token_type import TokenType
from typing import List
from token_parser.assignment_parser import AssignmentParser
from token_parser.definition_parser import DefinitionParser
from token_parser.expression_parser import ExpressionParser
from token_parser.if_parser import IfParser
from token_parser.return_parser import ReturnParser
from token_parser.while_parser import WhileParser

from tree_parser.node import Node
from tree_parser.node_type import NodeType
from lexer.token import TokenType, get_variable_types
from .base import BaseParser, are_next_tokens, eat_token


class StatementListParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        root = Node(NodeType.STATEMENT_LIST)
        statements = StatementListParser.get_statement_types()
        while (len(tokens) > 0) and not are_next_tokens(tokens, TokenType.END):
            token_type = tokens[0].token_type
            if token_type == TokenType.IDENTIFIER and tokens[1].token_type == TokenType.ASSIGN:
                token_type = (TokenType.IDENTIFIER, TokenType.ASSIGN)
            
            if (token_type in statements):
                root.add_child(statements[token_type].parse(tokens))
            else:
                raise ValueError(f"Expected statement but found {token_type} with lexeme \"{tokens[0].lexeme}\"")
            if (StatementListParser.semicolon_end(token_type) and are_next_tokens(tokens, TokenType.SEMICOLON)):
                eat_token(tokens, TokenType.SEMICOLON)
            elif (StatementListParser.semicolon_end(token_type) and not are_next_tokens(tokens, TokenType.SEMICOLON)) :
                raise ValueError(f"Expected ; but found {tokens[0].token_type} with lexeme \"{tokens[0].lexeme}\" on line {tokens[0].line_num}")
        return root

    @staticmethod
    def semicolon_end(token_type):
        require_semicolon = set({
            TokenType.RETURN,
            TokenType.DEF,
            TokenType.IDENTIFIER,
            (TokenType.IDENTIFIER, TokenType.ASSIGN)
        })
        return token_type in require_semicolon

    @staticmethod
    def get_statement_types():
        statements = dict({
            (TokenType.DEF): DefinitionParser,
            (TokenType.RETURN): ReturnParser,
            (TokenType.IDENTIFIER): ExpressionParser,
            (TokenType.IF): IfParser,
            (TokenType.WHILE): WhileParser,

            (TokenType.IDENTIFIER, TokenType.ASSIGN): AssignmentParser
        })
        return statements
    