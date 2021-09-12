from enum import Enum, auto

class NodeType(Enum):
    METHOD = auto()
    PARAMATER_LIST = auto()
    IDENTIFIER = auto()
    RETURN_TYPE = auto()
    TYPE = auto()
    STATEMENT_LIST = auto()
    STATEMENT = auto()
    EXPRESSION = auto()
    DEFINITION = auto()
    TERM = auto()
    NOT = auto()
    METHOD_CALL = auto()
    UNARY_OPERATION = auto()
    BNINARY_OPERATION = auto()
    OPERATION = auto()