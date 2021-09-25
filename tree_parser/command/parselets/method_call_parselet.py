from lexer.token_type import TokenType
from .prefix_parselet import PrefixParselet
from tree_parser.command.base_parser_cmd import BaseParserCmd
from lexer.token import Token
from command import CommandDelegate
import tree_parser as tp
from tree_parser import Node, NodeType

class MethodCallParselet(PrefixParselet):

    def parse(self, left: Node, token: Token, command: BaseParserCmd):
        node = Node(NodeType.METHOD_CALL, token)
        node.add_child(CommandDelegate.execute(tp.ExpressionCmd(command.tokens)).root)
        command.eat_token(TokenType.RPAREN)
        return node
    
