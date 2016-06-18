__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from WhileGrammarLexer import WhileGrammarLexer
from WhileGrammarParser import WhileGrammarParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = WhileGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileGrammarParser(token_stream)
    tree = parser.prog()

    tree_str = tree.toStringTree(recog=parser)
    print(tree_str)