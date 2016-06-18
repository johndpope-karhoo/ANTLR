from ArrayInitListener import ArrayInitListener
from ArrayInitParser import ArrayInitParser

class ArrayInitWalker(ArrayInitListener):
    def enterInit(self, ctx:ArrayInitParser.InitContext):
        pass

    # Exit a parse tree produced by ArrayInitParser#init.
    def exitInit(self, ctx:ArrayInitParser.InitContext):
        pass


    # Enter a parse tree produced by ArrayInitParser#value.
    def enterValue(self, ctx:ArrayInitParser.ValueContext):
        pass

    # Exit a parse tree produced by ArrayInitParser#value.
    def exitValue(self, ctx:ArrayInitParser.ValueContext):
        pass