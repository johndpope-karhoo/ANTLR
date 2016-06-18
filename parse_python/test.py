import sys
from antlr4 import *
from GrammarPyLexer import GrammarPyLexer
from GrammarPyParser import GrammarPyParser

def main(argv):
    istream = FileStream(argv[1])
    lexer = GrammarPyLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = GrammarPyParser(stream)
    tree = parser.init()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)