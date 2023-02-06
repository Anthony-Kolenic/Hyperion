from abc import ABC, abstractmethod
from typing import List
from lexer.token import Token
from lexer.token_type import TokenType
from tree_parser.node import Node

def eat_token(tokens: List[Token], *expected_tokens: TokenType) -> Token:
    token = tokens.pop(0)
    matches_types = False
    for current_token in expected_tokens:
        matches_types = matches_types or (token.token_type == current_token)
        
    if (not matches_types):
        raise ValueError(f"Expected token of type(s) {expected_tokens} but found {token.token_type} with lexeme \"{token.lexeme}\"")
    # print(f"Eating - {token}")
    return token

def are_next_tokens(tokens: List[Token], *token_types: TokenType) -> bool:
    # Check that there are enough tokens to validate against
    if (len(token_types) > len(tokens)):
        return False
    valid = True
    for index, token_type in enumerate(token_types):
        if (token_type != tokens[index].token_type):
            valid = False
            break
    return valid

def eat_any_token(tokens: List[Token]):
    return tokens.pop(0)

class BaseParser(ABC):
    @staticmethod
    @abstractmethod
    def parse(tokens: List[Token]) -> Node:
        ''''''
    
    


    
                    