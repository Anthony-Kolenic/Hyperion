from typing import List
from lexer.token_type import TokenType
from token_parser.base import are_next_tokens, eat_token
import token_parser
from .prefix_parselet import PrefixParselet
from lexer.token import Token
from command import CommandDelegate
import tree_parser as tp
from tree_parser import Node, NodeType

class MethodCallParselet(PrefixParselet):

    def parse(self, left: Node, _: Token, tokens: List[Token]):
        node = Node(NodeType.METHOD_CALL)
        node.add_child(left)
        while (not are_next_tokens(tokens, TokenType.RPAREN)):
            node.add_child(token_parser.ExpressionParser.parse(tokens))
            if (are_next_tokens(tokens, TokenType.COMMA)):
                eat_token(tokens, TokenType.COMMA)
        eat_token(tokens, TokenType.RPAREN)
        return node
    
