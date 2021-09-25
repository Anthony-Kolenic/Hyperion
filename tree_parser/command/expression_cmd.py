from tree_parser.command.parselets.precedence import Precedence
from typing import Callable, List, Dict
from tree_parser.node_type import NodeType
from lexer.token import Token, TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.node import Node
from .parselets import IdentifierParselet, PrefixOperatorParselet, GroupParselet, InfixOperatorParselet, Precedence, LiteralParselet, MethodCallParselet

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

    def __init__(self, tokens: List[Token], precedence: Precedence = Precedence.NONE):
        super().__init__(tokens)
        self.precedence = precedence
        self.pre_parslets: Dict[TokenType, Callable[..., Node]] = dict({})
        self.in_parslets: Dict[TokenType, Callable[..., Node]] = dict({})

        self.register_prefix(TokenType.IDENTIFIER, IdentifierParselet)
        
        self.register_prefix(TokenType.INT_LITERAL, LiteralParselet)
        self.register_prefix(TokenType.STR_LITERAL, LiteralParselet)
        self.register_prefix(TokenType.CHAR_LITERAL, LiteralParselet)
        self.register_prefix(TokenType.DBL_LITERAL, LiteralParselet)
        self.register_prefix(TokenType.BOOL_LITERAL, LiteralParselet)

        self.register_prefix(TokenType.ADD, PrefixOperatorParselet)
        self.register_prefix(TokenType.SUBTRACT, PrefixOperatorParselet)
        self.register_prefix(TokenType.NOT, PrefixOperatorParselet)
        self.register_prefix(TokenType.LPAREN, GroupParselet)

        self.register_infix(TokenType.ADD, InfixOperatorParselet, Precedence.SUM)
        self.register_infix(TokenType.SUBTRACT, InfixOperatorParselet, Precedence.SUM)
        self.register_infix(TokenType.MULTIPLY, InfixOperatorParselet, Precedence.PRODUCT)
        self.register_infix(TokenType.DIVIDE, InfixOperatorParselet, Precedence.PRODUCT)
        self.register_infix(TokenType.MOD, InfixOperatorParselet, Precedence.PRODUCT)
        self.register_infix(TokenType.LPAREN, MethodCallParselet, Precedence.CALL)

        self.register_infix(TokenType.AND, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.XOR, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.OR, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.GT, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.GTE, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.ST, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.STE, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.EQUALITY, InfixOperatorParselet, Precedence.CONDITIONAL)
        self.register_infix(TokenType.INEQUALITY, InfixOperatorParselet, Precedence.CONDITIONAL)

    def get_type(self):
        return NodeType.EXPRESSION

    def register_prefix(self, token_type: TokenType, parselet: Callable[..., Node]):
        self.pre_parslets[token_type] = parselet(Precedence.PREFIX)
    
    def register_infix(self, token_type: TokenType, parselet: Callable[..., Node], precedence):
        self.in_parslets[token_type] = parselet(precedence)

    def execute(self):
        token = self.eat_any_token()
        if (token.token_type in self.pre_parslets):
            left = self.pre_parslets[token.token_type].parse(token, self)
            while (self.precedence.value < self.get_precedence().value):
                token = self.eat_any_token()
                left = self.in_parslets[token.token_type].parse(left, token, self)
            self.root = left 
        else:
            raise ValueError(f"Expected expression but found {self.tokens[0]} with lexeme \"{self.tokens[0].lexeme}\"")

    def get_precedence(self):
        return Precedence.NONE if self.tokens[0].token_type not in self.in_parslets else self.in_parslets[self.tokens[0].token_type].precedence
