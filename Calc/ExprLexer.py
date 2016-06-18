# Generated from while/WhileGrammar.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\22")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16A")
        buf.write("\n\16\r\16\16\16B\3\17\6\17F\n\17\r\17\16\17G\3\20\5\20")
        buf.write("K\n\20\3\20\3\20\3\21\6\21P\n\21\r\21\16\21Q\3\21\3\21")
        buf.write("\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22\3\2\5\4\2C\\c|\3\2\62")
        buf.write(";\4\2\13\13\"\"X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13/\3")
        buf.write("\2\2\2\r\61\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\23\67")
        buf.write("\3\2\2\2\259\3\2\2\2\27;\3\2\2\2\31=\3\2\2\2\33@\3\2\2")
        buf.write("\2\35E\3\2\2\2\37J\3\2\2\2!O\3\2\2\2#$\7?\2\2$\4\3\2\2")
        buf.write("\2%&\7*\2\2&\6\3\2\2\2\'(\7+\2\2(\b\3\2\2\2)*\7y\2\2*")
        buf.write("+\7j\2\2+,\7k\2\2,-\7n\2\2-.\7g\2\2.\n\3\2\2\2/\60\7}")
        buf.write("\2\2\60\f\3\2\2\2\61\62\7\177\2\2\62\16\3\2\2\2\63\64")
        buf.write("\7@\2\2\64\20\3\2\2\2\65\66\7>\2\2\66\22\3\2\2\2\678\7")
        buf.write(",\2\28\24\3\2\2\29:\7\61\2\2:\26\3\2\2\2;<\7-\2\2<\30")
        buf.write("\3\2\2\2=>\7/\2\2>\32\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2C\34\3\2\2\2DF\t\3\2\2ED\3\2")
        buf.write("\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\36\3\2\2\2IK\7\17")
        buf.write("\2\2JI\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7\f\2\2M \3\2\2\2")
        buf.write("NP\t\4\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3")
        buf.write("\2\2\2ST\b\21\2\2T\"\3\2\2\2\7\2BGJQ\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    GREATER = 7
    LESS = 8
    MUL = 9
    DIV = 10
    ADD = 11
    SUB = 12
    ID = 13
    INT = 14
    NEWLINE = 15
    WS = 16

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'while'", "'{'", "'}'", "'>'", "'<'", 
            "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "GREATER", "LESS", "MUL", "DIV", "ADD", "SUB", "ID", "INT", 
            "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "GREATER", 
                  "LESS", "MUL", "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", 
                  "WS" ]

    grammarFileName = "WhileGrammar.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


