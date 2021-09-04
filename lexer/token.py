from .token_type import TokenType

class Token():
    def __init__(self, token_type: TokenType, lexeme: str):
        self.token_type = token_type
        self.lexeme = lexeme

    def __repr__(self) -> str:
        kvps = [f"{k}={v}" for k, v in vars(self).items()]
        return f"{type(self).__name__}({', '.join(kvps)})"