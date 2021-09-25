import tree_parser
from .prefix_parselet import PrefixParselet
from tree_parser.command.base_parser_cmd import BaseParserCmd
from lexer.token import Token
from command import CommandDelegate
import tree_parser
from tree_parser import Node, NodeType
from .precedence import Precedence

class PrefixOperatorParselet(PrefixParselet):
    def parse(self, token: Token, command: BaseParserCmd):
        node = Node(NodeType.UNARY_OPERATION, token)
        node.add_child(CommandDelegate.execute(tree_parser.ExpressionCmd(command.tokens, self.precedence)).root)
        return node
    
