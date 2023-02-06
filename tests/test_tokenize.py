from typing import Deque
import unittest

from lexer.token import Token
from lexer.token_type import TokenType
from main import tokenize

class TestTokenizer(unittest.TestCase):
    
    def test_tokenizer(self):
        """
        Test that validates route parser for empty function
        """
        chars = Deque(["i","f", "d","\n"])
        expected = [Token(TokenType.IDENTIFIER, lexeme="ifd")]
        tokens = tokenize(chars)
        self.assertEqual(expected, tokens)

if __name__ == '__main__':
    unittest.main()