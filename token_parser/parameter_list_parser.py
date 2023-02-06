from lexer.token import Token
from lexer.token_type import TokenType
from typing import List

from tree_parser.node import Node
from tree_parser.node_type import NodeType
from lexer.token import TokenType, get_variable_types
from .base import BaseParser, are_next_tokens, eat_token

class ParameterListParser(BaseParser):

    def parse(tokens: List[Token]) -> Node:
        root = Node(NodeType.PARAMETER_LIST)
        while (len(tokens) > 0 and not are_next_tokens(tokens, TokenType.RPAREN)):
            if (are_next_tokens(tokens, TokenType.VOID)):
                eat_token(tokens, TokenType.VOID)
            else:
                node = Node(NodeType.PARAMETER)
                node.add_child(Node(NodeType.IDENTIFIER, eat_token(tokens, TokenType.IDENTIFIER)))
                eat_token(tokens, TokenType.COLON)
                node.add_child(Node(NodeType.TYPE, eat_token(tokens, *get_variable_types())))
                root.add_child(node) 
                if (are_next_tokens(tokens, TokenType.COMMA)):
                    eat_token(tokens, TokenType.COMMA)
        return root
    
    