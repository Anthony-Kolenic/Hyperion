from .expression_graph import ExpressionGraph, Node
from .token_type import TokenType

def create_int_literal() -> ExpressionGraph:
    result = ExpressionGraph(TokenType.INT_LITERAL)
    for i in range(10):
        result.root.connections[str(i)] = Node(True)

    for k,v in result.root.connections.items(): # for each connection
        for a,b in result.root.connections.items(): # connect every other connection
            v.connections[a] = b
    return result

def create_dbl_literal() -> ExpressionGraph:
    result = ExpressionGraph(TokenType.DBL_LITERAL)
    for i in range(10):
        result.root.connections[str(i)] = Node(False)

    for k,v in result.root.connections.items(): # for each connection
        for a,b in result.root.connections.items(): # connect every other connection
            v.connections[a] = b
    # add dot
    periodNode = Node(False)
    for k,v in result.root.connections.items(): # for each connection
        v.connections['.'] = periodNode
    
    for i in range(10):
        periodNode.connections[str(i)] = Node(True)

    for k,v in periodNode.connections.items(): # for each connection
        for a,b in periodNode.connections.items(): # connect every other connection
            v.connections[a] = b
    return result

def create_char_literal() -> ExpressionGraph:
    result = ExpressionGraph(TokenType.CHAR_LITERAL)
    root = result.root
    delimiter = "'"
    root.connections[delimiter] = Node(False)
    for i in range(32,128):
        if i is not ord("'"):
            root.connections[delimiter].connections[chr(i)] = Node(False)
    finalNode = Node(True)
    for node in root.connections[delimiter].connections.values():
        node.connections[delimiter] = finalNode
    return result

def create_string_literal() -> ExpressionGraph:
    result = ExpressionGraph(TokenType.STR_LITERAL)
    root = result.root
    delimiter = '"'
    root.connections[delimiter] = Node(False)
    for i in range(32,128):
        if i is not ord(delimiter):
            root.connections[delimiter].connections[chr(i)] = Node(False)
    
    for k,v in root.connections[delimiter].connections.items(): # for each connection
        for a,b in root.connections[delimiter].connections.items(): # connect every other connection
            v.connections[a] = b
    
    finalNode = Node(True)
    for node in root.connections[delimiter].connections.values():
        node.connections[delimiter] = finalNode
    return result

def create_bool_lit() -> ExpressionGraph:
    result = ExpressionGraph(TokenType.BOOL_LITERAL)
    true_graph = create_keyword(TokenType.BOOL_LITERAL, "true")
    false_graph = create_keyword(TokenType.BOOL_LITERAL, "false")
    result.root.connections[list(true_graph.root.connections.keys())[0]] = list(true_graph.root.connections.values())[0]
    result.root.connections[list(false_graph.root.connections.keys())[0]] = list(false_graph.root.connections.values())[0]
    return result

def create_identifier() -> ExpressionGraph:
    result = ExpressionGraph(TokenType.IDENTIFIER)
    for i in range(ord('a'), ord('z') + 1):
        result.root.connections[chr(i)] = Node(True)
    for i in range(ord('A'), ord('Z') + 1):
        result.root.connections[chr(i)] = Node(True)
    result.root.connections["_"] = Node(True)
    for _,v in result.root.connections.items(): # for each connection
        for a,b in result.root.connections.items(): # connect every other connection
            v.connections[a] = b
    return result

def create_keyword(token_type: TokenType, keyword: str):
    result = ExpressionGraph(token_type)
    current_node = result.root
    for letter in keyword:
        next_node = Node()
        current_node.connections[letter] = next_node
        current_node = next_node
    current_node.final = True
    return result

def get_expression_list():
    result = []
    result.append(create_keyword(TokenType.ADD, '+'))
    result.append(create_keyword(TokenType.EQUALITY, "=="))

    result.append(create_keyword(TokenType.AND, "and"))
    result.append(create_keyword(TokenType.ASSIGN, "="))
    result.append(create_keyword(TokenType.BEGIN, "{"))
    result.append(create_keyword(TokenType.BOOL, "bool"))
    result.append(create_bool_lit())
    result.append(create_keyword(TokenType.CHAR, "char"))
    result.append(create_char_literal())
    result.append(create_keyword(TokenType.COLON, ":"))
    result.append(create_keyword(TokenType.COMMA, ","))
    result.append(create_keyword(TokenType.DBL, "double"))
    result.append(create_dbl_literal())
    result.append(create_keyword(TokenType.DEF, "def"))
    result.append(create_keyword(TokenType.DIVIDE, "/"))
    result.append(create_keyword(TokenType.DO, "do"))
    result.append(create_keyword(TokenType.ELSE, "else"))
    result.append(create_keyword(TokenType.END, "}"))
    result.append(create_keyword(TokenType.GT, ">"))
    result.append(create_keyword(TokenType.GTE, ">="))
    result.append(create_keyword(TokenType.IF, "if"))
    result.append(create_keyword(TokenType.ELSE_IF, "elif"))
    result.append(create_keyword(TokenType.INEQUALITY, "!="))
    result.append(create_keyword(TokenType.INT, "int"))
    result.append(create_int_literal())
    result.append(create_keyword(TokenType.LPAREN, "("))
    result.append(create_keyword(TokenType.LSPAREN, "["))
    result.append(create_keyword(TokenType.MOD, "%"))
    result.append(create_keyword(TokenType.MULTIPLY, "*"))
    result.append(create_keyword(TokenType.NONE, "none"))
    result.append(create_keyword(TokenType.NOT, "!"))
    result.append(create_keyword(TokenType.OR, "or"))
    result.append(create_keyword(TokenType.RETURN, "return"))
    result.append(create_keyword(TokenType.ROUTE, "route"))
    result.append(create_keyword(TokenType.RPAREN, ")"))
    result.append(create_keyword(TokenType.RSPAREN, "]"))
    result.append(create_keyword(TokenType.SEMICOLON, ";"))
    result.append(create_keyword(TokenType.ST, "<"))
    result.append(create_keyword(TokenType.STE, "<="))
    result.append(create_keyword(TokenType.STRING, "string"))
    result.append(create_string_literal()) 
    result.append(create_keyword(TokenType.SUBTRACT, "-"))
    result.append(create_keyword(TokenType.VOID, "nothing"))
    result.append(create_keyword(TokenType.WHILE, "while"))
    result.append(create_keyword(TokenType.XOR, "xor"))
    result.append(create_identifier())
    return result

