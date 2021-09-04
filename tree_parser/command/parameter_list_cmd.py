from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.node import Node
from tree_parser.node_type import NodeType

class ParameterListCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.PARAMATER_LIST

    def execute(self):
        while (len(self.tokens) > 0 and not self.is_next_token(TokenType.RPAREN)):
            if (self.is_next_token(TokenType.VOID)):
                self.eat_token(TokenType.VOID)
            else:
                self.root.add_child(Node(NodeType.IDENTIFIER, self.eat_token( TokenType.IDENTIFIER )))
                self.eat_token(TokenType.COLON)
                self.root.add_child(Node(NodeType.TYPE, self.eat_token(TokenType.INT, TokenType.BOOL, TokenType.CHAR, TokenType.STRING, TokenType.DBL))) # TODO: Allow any type
                if (self.is_next_token(TokenType.COMMA)):
                    self.eat_token(TokenType.COMMA)


