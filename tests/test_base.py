import unittest

from lexer.token import Token
from lexer.token_type import TokenType
from token_parser import RouteParser
from tree_parser import NodeType, Node

class TestRouteParser(unittest.TestCase):
    
    def test_empty(self):
        """
        Test that validates route parser for empty function
        """
        tokens = [
            Token(TokenType.ROUTE, "route"),
            Token(TokenType.IDENTIFIER, "test"),
            Token(TokenType.LPAREN, "("),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.COLON, ":"),
            Token(TokenType.INT, "uint64"),
            Token(TokenType.BEGIN, "{"),
            Token(TokenType.END, "}"),

        ]
        node = RouteParser.parse(tokens)
        expected = [NodeType.IDENTIFIER, NodeType.PARAMETER_LIST, NodeType.RETURN_TYPE, NodeType.STATEMENT_LIST]
        self.assertEqual(len(node.children), len(expected))
        for i, node in enumerate(node.children):
            self.assertEqual(node.node_type, expected[i])
    
    def test_parameter_list(self):
        """
        Test that validates route parser for function with parameter list
        """
        tokens = [
            Token(TokenType.ROUTE, "route"),
            Token(TokenType.IDENTIFIER, "test"),
            Token(TokenType.LPAREN, "("),
            Token(TokenType.IDENTIFIER, "x"),
            Token(TokenType.COLON, ":"),
            Token(TokenType.INT, "int"),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.COLON, ":"),
            Token(TokenType.INT, "uint64"),
            Token(TokenType.BEGIN, "{"),
            Token(TokenType.END, "}"),

        ]
        node = RouteParser.parse(tokens)
        expected = [NodeType.IDENTIFIER, NodeType.PARAMETER_LIST, NodeType.RETURN_TYPE, NodeType.STATEMENT_LIST]
        self.assertEqual(len(node.children), len(expected))
        for i, node in enumerate(node.children):
            self.assertEqual(node.node_type, expected[i])

if __name__ == '__main__':
    unittest.main()