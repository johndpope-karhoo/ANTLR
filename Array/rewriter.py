from ArrayInitListener import ArrayInitListener


class RewriteListener(ArrayInitListener):
    # Enter a parse tree produced by ArrayInitParser#init.
    def enterInit(self, ctx):
        print("(")

    # Exit a parse tree produced by ArrayInitParser#init.
    def exitInit(self, ctx):
        print(")")

    # Enter a parse tree produced by ArrayInitParser#value.
    def enterValue(self, ctx):
        print(',')

    # Exit a parse tree produced by ArrayInitParser#value.
    def exitValue(self, ctx):
        data = ctx.INT().getText()
        print(data)