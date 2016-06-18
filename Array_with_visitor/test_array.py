import sys
from antlr4 import *
from ArrayInitLexer import ArrayInitLexer
from ArrayInitParser import ArrayInitParser
from ArrayInitVisitor import ArrayInitVisitor

def main(argv):
    istream = FileStream(argv[1])
    lexer = ArrayInitLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = ArrayInitParser(stream)
    tree = parser.init()
    print(tree.toStringTree(recog=parser))

    visitor = ArrayInitVisitor()
    print(visitor.visit(tree))

if __name__ == '__main__':
    main(sys.argv)