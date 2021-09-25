from .prefix_parselet import PrefixParselet
from tree_parser.command.base_parser_cmd import BaseParserCmd
from lexer.token import Token
from command import CommandDelegate
import tree_parser as tp
from tree_parser import Node, NodeType

class InfixOperatorParselet(PrefixParselet):

    def parse(self, left: Node, token: Token, command: BaseParserCmd):
        node = Node(NodeType.BINARY_OPERATION, token)
        node.add_child(left)
        node.add_child(CommandDelegate.execute(tp.ExpressionCmd(command.tokens, self.precedence)).root)
        return node
    
