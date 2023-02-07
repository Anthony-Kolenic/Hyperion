from lexer.token import Token
from lexer.token_type import TokenType
from typing import List, Dict, Callable
from .parselets import IdentifierParselet, PrefixOperatorParselet, GroupParselet, InfixOperatorParselet, Precedence, LiteralParselet, MethodCallParselet, Precedence
from .base import BaseParser,  eat_any_token
from tree_parser.node import Node
from tree_parser.node_type import NodeType

""" Expression Parser, deals with an expression. 
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
class ExpressionParser(BaseParser):
    pre_parslets: Dict[TokenType, Callable[..., Node]] = {
        TokenType.IDENTIFIER: IdentifierParselet(Precedence.PREFIX),
        TokenType.INT_LITERAL: LiteralParselet(Precedence.PREFIX),
        TokenType.STR_LITERAL: LiteralParselet(Precedence.PREFIX),
        TokenType.CHAR_LITERAL: LiteralParselet(Precedence.PREFIX),
        TokenType.DBL_LITERAL: LiteralParselet(Precedence.PREFIX),
        TokenType.BOOL_LITERAL: LiteralParselet(Precedence.PREFIX),
        TokenType.ADD: PrefixOperatorParselet(Precedence.PREFIX),
        TokenType.SUBTRACT: PrefixOperatorParselet(Precedence.PREFIX),
        TokenType.NOT: PrefixOperatorParselet(Precedence.PREFIX),
        TokenType.LPAREN: GroupParselet(Precedence.PREFIX),
    } 

    in_parslets: Dict[TokenType, Callable[..., Node]] = {
        TokenType.ADD: InfixOperatorParselet(Precedence.SUM),
        TokenType.SUBTRACT: InfixOperatorParselet(Precedence.SUM),
        TokenType.MULTIPLY: InfixOperatorParselet(Precedence.PRODUCT),
        TokenType.DIVIDE: InfixOperatorParselet(Precedence.PRODUCT),
        TokenType.MOD: InfixOperatorParselet(Precedence.PRODUCT),

        TokenType.AND: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.XOR: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.OR: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.GT: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.GTE: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.ST: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.STE: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.EQUALITY: InfixOperatorParselet(Precedence.CONDITIONAL),
        TokenType.INEQUALITY: InfixOperatorParselet(Precedence.CONDITIONAL),

        TokenType.LPAREN: MethodCallParselet(Precedence.CALL),
    }

    def parse(tokens: List[Token], precedence: int = Precedence.NONE) -> Node:
        token = eat_any_token(tokens)
        node = Node(NodeType.EXPRESSION)
        if (token.token_type in ExpressionParser.pre_parslets):
            left = ExpressionParser.pre_parslets[token.token_type].parse(token, tokens)
            while (precedence.value < ExpressionParser.get_precedence(tokens).value):
                token = eat_any_token(tokens)
                left = ExpressionParser.in_parslets[token.token_type].parse(left, token, tokens)
            node.add_child(left) 
        else:
            raise ValueError(f"Expected expression but found {tokens[0]} with lexeme \"{tokens[0].lexeme}\" line {tokens[0].line_num}")
        return node

        
    @staticmethod
    def get_precedence( tokens):
        return Precedence.NONE if tokens[0].token_type not in ExpressionParser.in_parslets else ExpressionParser.in_parslets[tokens[0].token_type].precedence

    
    