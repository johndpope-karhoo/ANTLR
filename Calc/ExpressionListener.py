# Generated from LabeledExpr.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete listener for a parse tree produced by ExpressionParser.
class LabeledExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#prog.
    def enterProg(self, ctx:ExpressionParser.ProgContext):
        pass

    # Exit a parse tree produced by ExpressionParser#prog.
    def exitProg(self, ctx:ExpressionParser.ProgContext):
        pass


    # Enter a parse tree produced by ExpressionParser#printExpr.
    def enterPrintExpr(self, ctx:ExpressionParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#printExpr.
    def exitPrintExpr(self, ctx:ExpressionParser.PrintExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#assign.
    def enterAssign(self, ctx:ExpressionParser.AssignContext):
        pass

    # Exit a parse tree produced by ExpressionParser#assign.
    def exitAssign(self, ctx:ExpressionParser.AssignContext):
        pass


    # Enter a parse tree produced by ExpressionParser#blank.
    def enterBlank(self, ctx:ExpressionParser.BlankContext):
        pass

    # Exit a parse tree produced by ExpressionParser#blank.
    def exitBlank(self, ctx:ExpressionParser.BlankContext):
        pass


    # Enter a parse tree produced by ExpressionParser#parens.
    def enterParens(self, ctx:ExpressionParser.ParensContext):
        pass

    # Exit a parse tree produced by ExpressionParser#parens.
    def exitParens(self, ctx:ExpressionParser.ParensContext):
        pass


    # Enter a parse tree produced by ExpressionParser#MulDiv.
    def enterMulDiv(self, ctx:ExpressionParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExpressionParser#MulDiv.
    def exitMulDiv(self, ctx:ExpressionParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExpressionParser#AddSub.
    def enterAddSub(self, ctx:ExpressionParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExpressionParser#AddSub.
    def exitAddSub(self, ctx:ExpressionParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExpressionParser#id.
    def enterId(self, ctx:ExpressionParser.IdContext):
        pass

    # Exit a parse tree produced by ExpressionParser#id.
    def exitId(self, ctx:ExpressionParser.IdContext):
        pass


    # Enter a parse tree produced by ExpressionParser#int.
    def enterInt(self, ctx:ExpressionParser.IntContext):
        pass

    # Exit a parse tree produced by ExpressionParser#int.
    def exitInt(self, ctx:ExpressionParser.IntContext):
        pass


