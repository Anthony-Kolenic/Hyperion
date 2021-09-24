from typing import Callable, List, Dict
from tree_parser.node_type import NodeType
from lexer.token import Token, TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from command.command_delegate import CommandDelegate
from tree_parser.node import Node
from abc import ABC, abstractmethod

class PrefixParselet(ABC):

    def __init__(self, precedence):
        self.precedence = precedence

    @abstractmethod
    def parse(self, token):
        pass

class InfixParselet(ABC):

    def __init__(self, precedence):
        self.precedence = precedence

    @abstractmethod
    def parse(self, left, token):
        pass

class IdentifierParselet(PrefixParselet):
    @staticmethod
    def parse(_,token, __ ):
        return Node(NodeType.IDENTIFIER, token)


class PrefixOperatorParselet(PrefixParselet):
    @staticmethod
    def parse(tokens, token, precendece):
        node = Node(NodeType.UNARY_OPERATION, token)
        node.add_child(CommandDelegate.execute(ExpressionCmd(tokens, precendece)).root)
        return node

class GroupParselet(PrefixParselet):
    @staticmethod
    def parse(tokens, token, _):
        node = CommandDelegate.execute(ExpressionCmd(tokens)).root
        tokens.pop(0)
        return node

class InfixOperatorParselet(InfixParselet):
    @staticmethod
    def parse(precedence, tokens, left, token):
        node = Node(NodeType.BINARY_OPERATION, token)
        node.add_child(left)
        node.add_child(CommandDelegate.execute(ExpressionCmd(tokens, precedence)).root)
        return node

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

    def __init__(self, tokens: List[Token], precedence: int = 0):
        super().__init__(tokens)
        self.precedence = precedence
        self.pre_parslets: Dict[TokenType, Callable[..., Node]] = dict({})
        self.in_parslets: Dict[TokenType, Callable[..., Node]] = dict({})

        self.register_prefix(TokenType.IDENTIFIER, IdentifierParselet)
        self.register_prefix(TokenType.ADD, PrefixOperatorParselet)
        self.register_prefix(TokenType.SUBTRACT, PrefixOperatorParselet)
        self.register_prefix(TokenType.NOT, PrefixOperatorParselet)
        self.register_prefix(TokenType.LPAREN, GroupParselet)

        self.register_infix(TokenType.ADD, InfixOperatorParselet, 3)
        self.register_infix(TokenType.SUBTRACT, InfixOperatorParselet, 3)
        self.register_infix(TokenType.MULTIPLY, InfixOperatorParselet, 4)

    def get_type(self):
        return NodeType.EXPRESSION

    def register_prefix(self, token_type: TokenType, parselet: Callable[..., Node]):
        self.pre_parslets[token_type] = parselet(6)
    
    def register_infix(self, token_type: TokenType, parselet: Callable[..., Node], precedence):
        self.in_parslets[token_type] = parselet(precedence)

    def execute(self):
        token = self.eat_any_token()
        if (token.token_type in self.pre_parslets):
            left = self.pre_parslets[token.token_type].parse(self.tokens, token, self.pre_parslets[token.token_type].precedence)
            while (self.precedence < self.get_precedence()):
                token = self.eat_any_token()
                left = self.in_parslets[token.token_type].parse(self.in_parslets[token.token_type].precedence, self.tokens, left, token)
            self.root = left 
        else:
            raise ValueError(f"Expected expression but found {self.tokens[0]} with lexeme \"{self.tokens[0].lexeme}\"")

    def get_precedence(self):
        return 0 if self.tokens[0].token_type not in self.in_parslets else self.in_parslets[self.tokens[0].token_type].precedence

    @staticmethod
    def operators():
        return [TokenType.ADD, TokenType.SUBTRACT, TokenType.MULTIPLY, TokenType.DIVIDE];