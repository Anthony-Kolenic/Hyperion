from lexer.token import Token
from lexer.token_type import TokenType
from typing import List
from token_parser import expression_parser

from tree_parser.node import Node
from tree_parser.node_type import NodeType
from .base import BaseParser, are_next_tokens, eat_token
from lexer.token import TokenType, get_variable_types

class DefinitionParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        root = Node(NodeType.DEFINITION)

        eat_token(tokens, TokenType.DEF)
        root.add_child(Node(NodeType.IDENTIFIER, eat_token(tokens, TokenType.IDENTIFIER)))
        eat_token(tokens, TokenType.COLON)
        root.add_child(Node(NodeType.TYPE, eat_token(tokens, *get_variable_types())))
        if (are_next_tokens(tokens, TokenType.ASSIGN)):
            eat_token(tokens, TokenType.ASSIGN)
            root.add_child(expression_parser.parse(tokens))
        
        
        return root
    
    