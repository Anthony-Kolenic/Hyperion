from typing import Deque, List
from lexer.token_type import TokenType
from lexer.token import Token
from lexer.expressions  import *
from tree_parser.command_delegate import CommandDelegate
from tree_parser.command.parse_cmd import ParseCmd

def main():
    print("====\t Reading File \t====")
    file_text = ""
    with open('data/test.txt', "r") as f:
        file_text = f.read()
    characters = Deque()
    for character in file_text:
        characters.append(character)

    print("====\t Tokenizing \t====\n")
    tokens = tokenize(characters)
    for token in tokens:
        print(f"({token.token_type}: {token.lexeme})")

    print("\n====\t Parsing \t====\n")
    parserCmd = CommandDelegate.execute(ParseCmd(tokens))
    print(parserCmd.root)

def tokenize(characters: Deque) -> List[Token]:
    graphs = get_expression_list()
    tokens = []
    all_chars_processed = False
    while not all_chars_processed:
        # initialize starting variables, reset graphs to start positions
        lexeme = ""
        characters = remove_whitespace(characters)
        all_chars_processed = len(characters) == 0
        for graph in graphs:
                graph.reset()
        # if there are characters on the deque, read them one by one until all the graphs are in a failed state.
        # Once all have failed, find the graph with the smallest match length. That is the token
        if (not all_chars_processed):
            all_failed = False
            while not all_failed:
                current_char = characters[0]
                for graph in graphs:
                    graph.process(current_char)

                all_failed = True not in [graph.in_match_state for graph in graphs]           
                if (not all_failed):
                    lexeme += current_char
                    characters.popleft()

            # find best matching graph
            best_graph = None
            for graph in graphs:
                if (best_graph == None and graph.ended()) or (best_graph == None and graph.ended() and graph.match_length > best_graph.match_length):
                    best_graph = graph

            if (best_graph != None):
                tokens.append(Token(best_graph.token_type, lexeme))
            else:
                raise ValueError(f"Unknown character sequence {lexeme}")
    return tokens

def remove_whitespace(characters: Deque) -> Deque:
    while (len(characters) > 0 and characters[0].isspace()):
        characters.popleft()
    return characters;

if __name__ == "__main__":
    main()