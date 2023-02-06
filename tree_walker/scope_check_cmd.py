from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from command.base_cmd import BaseCmd
from tree_parser import Node, NodeType
from typing import Callable, Dict
from itertools import count

@dataclass
class ScopeTable():
    table: Dict[str, str] = field(default_factory=lambda: {})
    parent: int = None

class ScopeCheckCmd(BaseCmd):
    counter = count(1)
    def __init__(self, root):
        self.root = root
        self.depth = 0
        
    def execute(self):
        root = "root"
        scope: Dict[str, ScopeTable] = {root : ScopeTable()}
        self.node_map: Dict[NodeType, Callable[[ScopeCheckCmd, Dict[int, ScopeTable], Node, str]]] = {
            NodeType.METHOD: self.handle_method,
            NodeType.DEFINITION: self.handle_definition,
            NodeType.WHILE_LOOP: self.handle_structure,
            NodeType.CONDITIONAL: self.handle_structure,
            NodeType.ELSE: self.handle_structure,
        }
        self.walk_children(scope, self.root, root)
        print(scope)
        

    def walk_children(self, scope: Dict[int, ScopeTable], node: Node, level: str):
        for child in node.children:
            if child.node_type in self.node_map:
                print(child.node_type)
                self.node_map[child.node_type](scope, child, level)

    def handle_method(self, scope: Dict[int, ScopeTable], node: Node, level: str):
        identifier = node.get_child_by_type(NodeType.IDENTIFIER).token.lexeme
        scope[level].table[identifier] = "function"
        function_scope = ScopeTable(parent=level)
        parameters = node.get_child_by_type(NodeType.PARAMETER_LIST).children
        for parameter in parameters:
            param_name = parameter.get_child_by_type(NodeType.IDENTIFIER).token.lexeme
            param_type = parameter.get_child_by_type(NodeType.TYPE).token.token_type
            function_scope.table[param_name] = param_type
        scope[identifier] = function_scope
        statements = node.get_child_by_type(NodeType.STATEMENT_LIST)
        self.walk_children(scope, statements, identifier)

    def handle_definition(self, scope: Dict[int, ScopeTable], node: Node, level: str):
        identifier = node.get_child_by_type(NodeType.IDENTIFIER).token.lexeme
        scope[level].table[identifier] = node.get_child_by_type(NodeType.TYPE).token.token_type

    def handle_structure(self, scope: Dict[int, ScopeTable], node: Node, level: str):
        for child in node.children:
            if child.node_type == NodeType.STATEMENT_LIST:
                inner_scope = ScopeTable(parent=level)
                key = f"{level}_{next(ScopeCheckCmd.counter)}"
                scope[key] = inner_scope
                self.walk_children(scope, child, key)

        