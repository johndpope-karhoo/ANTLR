__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from ExpressionLexer import ExpressionLexer
from ExpressionParser import ExpressionParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = ExpressionLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExpressionParser(token_stream)
    tree = parser.prog()

    tree_str = tree.toStringTree(recog=parser)
    print(tree_str)