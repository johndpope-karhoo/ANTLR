# Generated from WhileGrammar.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\20")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4*\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\62\n\4\f\4\16")
        buf.write("\4\65\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6>\n\6\3\6\7")
        buf.write("\6A\n\6\f\6\16\6D\13\6\3\6\2\3\6\7\2\4\6\b\n\2\5\3\2\t")
        buf.write("\n\3\2\13\f\3\2\7\bK\2\r\3\2\2\2\4 \3\2\2\2\6)\3\2\2\2")
        buf.write("\b\66\3\2\2\2\n:\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17")
        buf.write("\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\3\3\2\2\2\21\22")
        buf.write("\5\6\4\2\22\23\7\17\2\2\23!\3\2\2\2\24\25\7\r\2\2\25\26")
        buf.write("\7\3\2\2\26\27\5\6\4\2\27\30\7\17\2\2\30!\3\2\2\2\31\32")
        buf.write("\5\n\6\2\32\33\7\17\2\2\33!\3\2\2\2\34\35\5\b\5\2\35\36")
        buf.write("\7\17\2\2\36!\3\2\2\2\37!\7\17\2\2 \21\3\2\2\2 \24\3\2")
        buf.write("\2\2 \31\3\2\2\2 \34\3\2\2\2 \37\3\2\2\2!\5\3\2\2\2\"")
        buf.write("#\b\4\1\2#*\7\16\2\2$*\7\r\2\2%&\7\4\2\2&\'\5\6\4\2\'")
        buf.write("(\7\5\2\2(*\3\2\2\2)\"\3\2\2\2)$\3\2\2\2)%\3\2\2\2*\63")
        buf.write("\3\2\2\2+,\f\7\2\2,-\t\2\2\2-\62\5\6\4\b./\f\6\2\2/\60")
        buf.write("\t\3\2\2\60\62\5\6\4\7\61+\3\2\2\2\61.\3\2\2\2\62\65\3")
        buf.write("\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\7\3\2\2\2\65\63")
        buf.write("\3\2\2\2\66\67\5\6\4\2\678\t\4\2\289\5\6\4\29\t\3\2\2")
        buf.write("\2:;\7\6\2\2;=\5\b\5\2<>\7\17\2\2=<\3\2\2\2=>\3\2\2\2")
        buf.write(">B\3\2\2\2?A\5\4\3\2@?\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3")
        buf.write("\2\2\2C\13\3\2\2\2DB\3\2\2\2\t\17 )\61\63=B")
        return buf.getvalue()


class WhileGrammarParser ( Parser ):

    grammarFileName = "WhileGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'while'", "'>'", 
                     "'<'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "GREATER", "LESS", "MUL", "DIV", "ADD", 
                      "SUB", "ID", "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_relational = 3
    RULE_loop = 4

    ruleNames =  [ "prog", "stat", "expr", "relational", "loop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    GREATER=5
    LESS=6
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    ID=11
    INT=12
    NEWLINE=13
    WS=14

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileGrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(WhileGrammarParser.StatContext,i)


        def getRuleIndex(self):
            return WhileGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = WhileGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << WhileGrammarParser.T__1) | (1 << WhileGrammarParser.T__3) | (1 << WhileGrammarParser.ID) | (1 << WhileGrammarParser.INT) | (1 << WhileGrammarParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileGrammarParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileLoopContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def loop(self):
            return self.getTypedRuleContext(WhileGrammarParser.LoopContext,0)

        def NEWLINE(self):
            return self.getToken(WhileGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)


    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(WhileGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class RelatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def relational(self):
            return self.getTypedRuleContext(WhileGrammarParser.RelationalContext,0)

        def NEWLINE(self):
            return self.getToken(WhileGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelat" ):
                listener.enterRelat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelat" ):
                listener.exitRelat(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileGrammarParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(WhileGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileGrammarParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(WhileGrammarParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(WhileGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = WhileGrammarParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 30
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = WhileGrammarParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(WhileGrammarParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = WhileGrammarParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(WhileGrammarParser.ID)
                self.state = 19
                self.match(WhileGrammarParser.T__0)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(WhileGrammarParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = WhileGrammarParser.WhileLoopContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.loop()
                self.state = 24
                self.match(WhileGrammarParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = WhileGrammarParser.RelatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.relational()
                self.state = 27
                self.match(WhileGrammarParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = WhileGrammarParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.match(WhileGrammarParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(WhileGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            token = self._input.LA(1)
            if token in [WhileGrammarParser.INT]:
                localctx = WhileGrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 33
                self.match(WhileGrammarParser.INT)

            elif token in [WhileGrammarParser.ID]:
                localctx = WhileGrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(WhileGrammarParser.ID)

            elif token in [WhileGrammarParser.T__1]:
                localctx = WhileGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(WhileGrammarParser.T__1)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(WhileGrammarParser.T__2)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = WhileGrammarParser.MulDivContext(self, WhileGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileGrammarParser.MUL or _la==WhileGrammarParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 43
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = WhileGrammarParser.AddSubContext(self, WhileGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileGrammarParser.ADD or _la==WhileGrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 46
                        self.expr(5)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RelationalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileGrammarParser.RULE_relational

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GreaterEqualContext(RelationalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.RelationalContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileGrammarParser.ExprContext,i)

        def GREATER(self):
            return self.getToken(WhileGrammarParser.GREATER, 0)
        def LESS(self):
            return self.getToken(WhileGrammarParser.LESS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEqual" ):
                listener.enterGreaterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEqual" ):
                listener.exitGreaterEqual(self)



    def relational(self):

        localctx = WhileGrammarParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relational)
        self._la = 0 # Token type
        try:
            localctx = WhileGrammarParser.GreaterEqualContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expr(0)
            self.state = 53
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==WhileGrammarParser.GREATER or _la==WhileGrammarParser.LESS):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 54
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileGrammarParser.RULE_loop

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileContext(LoopContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileGrammarParser.LoopContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def relational(self):
            return self.getTypedRuleContext(WhileGrammarParser.RelationalContext,0)

        def NEWLINE(self):
            return self.getToken(WhileGrammarParser.NEWLINE, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileGrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(WhileGrammarParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)



    def loop(self):

        localctx = WhileGrammarParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_loop)
        try:
            localctx = WhileGrammarParser.WhileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(WhileGrammarParser.T__3)

            self.state = 57
            self.relational()
            self.state = 59
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 58
                self.match(WhileGrammarParser.NEWLINE)


            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 61
                    self.stat() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




