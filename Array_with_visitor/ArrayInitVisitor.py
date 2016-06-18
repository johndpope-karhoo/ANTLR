# Generated from ArrayInit.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArrayInitParser import ArrayInitParser
else:
    from ArrayInitParser import ArrayInitParser

# This class defines a complete generic visitor for a parse tree produced by ArrayInitParser.

class ArrayInitVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArrayInitParser#init.
    def visitInit(self, ctx:ArrayInitParser.InitContext):
        print(self.visit(ctx))
        # if ctx.getText()[0] == "{":
        #     print("sddsfsf")
        #     return "[" + self.visitChildren(ctx) + "]"
        # else:
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArrayInitParser#value.
    def visitValue(self, ctx:ArrayInitParser.ValueContext):
        return self.visitChildren(ctx)



del ArrayInitParser


