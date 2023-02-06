from typing import Deque, List, Tuple
from lexer.token import Token
from lexer.expressions  import *
from command.command_delegate import CommandDelegate
from token_parser import FileParser
from tree_walker.scope_check_cmd import ScopeCheckCmd
from tree_walker.tree_output_cmd import TreeOutputCmd

import argparse

def main():
    parser = argparse.ArgumentParser()   
    parser.add_argument("-f", "--file", help="Text file to compile", required=True)
    parser.add_argument("-e", "--entry", help="Entry function", required=True)
    parser.add_argument("-d", "--debug", help="Output debug text", required=False, action="store_true", default=False)

    args = parser.parse_args()

    print("====\t Reading File \t====")
    file_text = ""
    with open(args.file, "r") as f:
        file_text = f.read()
    characters = Deque()
    for character in file_text:
        characters.append(character)

    print("====\t Tokenizing \t====")
    tokens = tokenize(characters)
    if args.debug:
        for token in tokens:
            print(f"({token.token_type}: {token.lexeme})")

    print("====\t Parsing \t====\n")
    root = FileParser.parse(tokens)
    if args.debug:
        ast = CommandDelegate.execute(TreeOutputCmd(root))
        print(ast.result())
    CommandDelegate.execute(ScopeCheckCmd(root))

def tokenize(characters: Deque) -> List[Token]:
    graphs = get_expression_list()
    tokens = []
    all_chars_processed = False
    line_num = 1
    while not all_chars_processed:
        # initialize starting variables, reset graphs to start positions
        lexeme = ""
        characters, lines = remove_whitespace(characters)
        line_num += lines
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
                if (best_graph == None and graph.ended() ) or (best_graph != None and graph.ended() and graph.match_length > best_graph.match_length ):
                    best_graph = graph

            if (best_graph != None):
                tokens.append(Token(best_graph.token_type, lexeme, line_num))
            else:
                raise ValueError(f"Unknown character sequence {lexeme} {characters} {line_num}")
    return tokens

def remove_whitespace(characters: Deque) -> Tuple[Deque, int]:
    lines = 0
    while (len(characters) > 0 and characters[0].isspace()):
        if characters[0] == "\n":
            lines += 1
        characters.popleft()
    return characters, lines;

if __name__ == "__main__":
    main()