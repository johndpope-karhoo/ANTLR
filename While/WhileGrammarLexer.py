# Generated from WhileGrammar.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\20")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\6\f9\n\f\r\f\16\f:\3\r\6\r>\n\r\r\r\16\r?\3")
        buf.write("\16\5\16C\n\16\3\16\3\16\3\17\6\17H\n\17\r\17\16\17I\3")
        buf.write("\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\3\2\5\4\2C\\c|\3\2\62")
        buf.write(";\4\2\13\13\"\"P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2")
        buf.write("\2\7#\3\2\2\2\t%\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17/\3")
        buf.write("\2\2\2\21\61\3\2\2\2\23\63\3\2\2\2\25\65\3\2\2\2\278\3")
        buf.write("\2\2\2\31=\3\2\2\2\33B\3\2\2\2\35G\3\2\2\2\37 \7?\2\2")
        buf.write(" \4\3\2\2\2!\"\7*\2\2\"\6\3\2\2\2#$\7+\2\2$\b\3\2\2\2")
        buf.write("%&\7y\2\2&\'\7j\2\2\'(\7k\2\2()\7n\2\2)*\7g\2\2*\n\3\2")
        buf.write("\2\2+,\7@\2\2,\f\3\2\2\2-.\7>\2\2.\16\3\2\2\2/\60\7,\2")
        buf.write("\2\60\20\3\2\2\2\61\62\7\61\2\2\62\22\3\2\2\2\63\64\7")
        buf.write("-\2\2\64\24\3\2\2\2\65\66\7/\2\2\66\26\3\2\2\2\679\t\2")
        buf.write("\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\30\3\2")
        buf.write("\2\2<>\t\3\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2")
        buf.write("@\32\3\2\2\2AC\7\17\2\2BA\3\2\2\2BC\3\2\2\2CD\3\2\2\2")
        buf.write("DE\7\f\2\2E\34\3\2\2\2FH\t\4\2\2GF\3\2\2\2HI\3\2\2\2I")
        buf.write("G\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\b\17\2\2L\36\3\2\2\2\7")
        buf.write("\2:?BI\3\b\2\2")
        return buf.getvalue()


class WhileGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    GREATER = 5
    LESS = 6
    MUL = 7
    DIV = 8
    ADD = 9
    SUB = 10
    ID = 11
    INT = 12
    NEWLINE = 13
    WS = 14

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'while'", "'>'", "'<'", "'*'", "'/'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "GREATER", "LESS", "MUL", "DIV", "ADD", "SUB", "ID", "INT", 
            "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "GREATER", "LESS", "MUL", 
                  "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", "WS" ]

    grammarFileName = "WhileGrammar.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


