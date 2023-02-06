from dataclasses import dataclass
from .token_type import *

@dataclass
class Token():
    token_type: TokenType
    lexeme: str
    line_num: int = 0 