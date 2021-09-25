from tree_parser.command.base_parser_cmd import BaseParserCmd
from .route_cmd import RouteCmd
from command.command_delegate import CommandDelegate
from tree_parser.node_type import NodeType

class ParseCmd(BaseParserCmd):
    def get_type(self) -> NodeType:
        return NodeType.ROOT

    def execute(self):
        while (len(self.tokens) > 0):
            self.root.add_child(CommandDelegate.execute(RouteCmd(self.tokens)).root)
            

