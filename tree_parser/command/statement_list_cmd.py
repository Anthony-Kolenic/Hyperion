from tree_parser.command.while_cmd import WhileCmd
from tree_parser.command.expression_cmd import ExpressionCmd
from command.command_delegate import CommandDelegate
from lexer.token import TokenType
from tree_parser.command.base_parser_cmd import BaseParserCmd
from tree_parser.command.return_cmd import ReturnCmd
from tree_parser.command.definition_cmd import DefinitionCmd
from tree_parser.command.assign_cmd import AssignCmd
from tree_parser.command.if_cmd import IfCmd
from tree_parser.command.while_cmd import WhileCmd
from tree_parser.node_type import NodeType

class StatementListCmd(BaseParserCmd):

    def get_type(self):
        return NodeType.STATEMENT_LIST

    def execute(self):
        statements = StatementListCmd.get_statement_types()
        while (len(self.tokens) > 0 and not self.is_next_token(TokenType.END)):
            token = self.tokens[0]
            if (token.token_type in statements):
                self.root.add_child(CommandDelegate.execute(statements[token.token_type](self.tokens)).root)
            elif (token.token_type == TokenType.IDENTIFIER):
                if (self.tokens[1].token_type == TokenType.ASSIGN):
                    self.root.add_child(CommandDelegate.execute(AssignCmd(self.tokens)).root)
                    self.eat_token(TokenType.SEMICOLON)
                elif (self.tokens[1].token_type == TokenType.LPAREN):
                    self.root.add_child(CommandDelegate.execute(ExpressionCmd(self.tokens)).root)
                    self.eat_token(TokenType.SEMICOLON)
                else:
                    raise ValueError(f"Expected statement but found {token.token_type} with lexeme \"{token.lexeme}\"")
            else:
                raise ValueError(f"Expected statement but found {token.token_type} with lexeme \"{token.lexeme}\"")

    @staticmethod
    def get_statement_types():
        statements = dict()
        statements[TokenType.RETURN] = ReturnCmd
        statements[TokenType.DEF] = DefinitionCmd
        statements[TokenType.IF] = IfCmd
        statements[TokenType.WHILE] = WhileCmd
        return statements
