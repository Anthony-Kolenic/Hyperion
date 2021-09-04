from .base_cmd import BaseCmd
from .route_cmd import RouteCmd
from ..command_delegate import CommandDelegate
from lexer.token import Token
from typing import List

class ParseCmd(BaseCmd):

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
    
    def execute(self):
        CommandDelegate.execute(RouteCmd(self.tokens))

