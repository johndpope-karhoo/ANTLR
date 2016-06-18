# Generated from GrammarPy.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarPyParser import GrammarPyParser
else:
    from GrammarPyParser import GrammarPyParser

# This class defines a complete listener for a parse tree produced by GrammarPyParser.
class GrammarPyListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarPyParser#single_input.
    def enterSingle_input(self, ctx:GrammarPyParser.Single_inputContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#single_input.
    def exitSingle_input(self, ctx:GrammarPyParser.Single_inputContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#file_input.
    def enterFile_input(self, ctx:GrammarPyParser.File_inputContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#file_input.
    def exitFile_input(self, ctx:GrammarPyParser.File_inputContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#eval_input.
    def enterEval_input(self, ctx:GrammarPyParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#eval_input.
    def exitEval_input(self, ctx:GrammarPyParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#decorator.
    def enterDecorator(self, ctx:GrammarPyParser.DecoratorContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#decorator.
    def exitDecorator(self, ctx:GrammarPyParser.DecoratorContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#decorators.
    def enterDecorators(self, ctx:GrammarPyParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#decorators.
    def exitDecorators(self, ctx:GrammarPyParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#decorated.
    def enterDecorated(self, ctx:GrammarPyParser.DecoratedContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#decorated.
    def exitDecorated(self, ctx:GrammarPyParser.DecoratedContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#funcdef.
    def enterFuncdef(self, ctx:GrammarPyParser.FuncdefContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#funcdef.
    def exitFuncdef(self, ctx:GrammarPyParser.FuncdefContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#parameters.
    def enterParameters(self, ctx:GrammarPyParser.ParametersContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#parameters.
    def exitParameters(self, ctx:GrammarPyParser.ParametersContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#typedargslist.
    def enterTypedargslist(self, ctx:GrammarPyParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#typedargslist.
    def exitTypedargslist(self, ctx:GrammarPyParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#tfpdef.
    def enterTfpdef(self, ctx:GrammarPyParser.TfpdefContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#tfpdef.
    def exitTfpdef(self, ctx:GrammarPyParser.TfpdefContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#varargslist.
    def enterVarargslist(self, ctx:GrammarPyParser.VarargslistContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#varargslist.
    def exitVarargslist(self, ctx:GrammarPyParser.VarargslistContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#vfpdef.
    def enterVfpdef(self, ctx:GrammarPyParser.VfpdefContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#vfpdef.
    def exitVfpdef(self, ctx:GrammarPyParser.VfpdefContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#stmt.
    def enterStmt(self, ctx:GrammarPyParser.StmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#stmt.
    def exitStmt(self, ctx:GrammarPyParser.StmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#simple_stmt.
    def enterSimple_stmt(self, ctx:GrammarPyParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#simple_stmt.
    def exitSimple_stmt(self, ctx:GrammarPyParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#small_stmt.
    def enterSmall_stmt(self, ctx:GrammarPyParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#small_stmt.
    def exitSmall_stmt(self, ctx:GrammarPyParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#expr_stmt.
    def enterExpr_stmt(self, ctx:GrammarPyParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#expr_stmt.
    def exitExpr_stmt(self, ctx:GrammarPyParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:GrammarPyParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:GrammarPyParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#augassign.
    def enterAugassign(self, ctx:GrammarPyParser.AugassignContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#augassign.
    def exitAugassign(self, ctx:GrammarPyParser.AugassignContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#del_stmt.
    def enterDel_stmt(self, ctx:GrammarPyParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#del_stmt.
    def exitDel_stmt(self, ctx:GrammarPyParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#pass_stmt.
    def enterPass_stmt(self, ctx:GrammarPyParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#pass_stmt.
    def exitPass_stmt(self, ctx:GrammarPyParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#flow_stmt.
    def enterFlow_stmt(self, ctx:GrammarPyParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#flow_stmt.
    def exitFlow_stmt(self, ctx:GrammarPyParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#break_stmt.
    def enterBreak_stmt(self, ctx:GrammarPyParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#break_stmt.
    def exitBreak_stmt(self, ctx:GrammarPyParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#continue_stmt.
    def enterContinue_stmt(self, ctx:GrammarPyParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#continue_stmt.
    def exitContinue_stmt(self, ctx:GrammarPyParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#return_stmt.
    def enterReturn_stmt(self, ctx:GrammarPyParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#return_stmt.
    def exitReturn_stmt(self, ctx:GrammarPyParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#yield_stmt.
    def enterYield_stmt(self, ctx:GrammarPyParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#yield_stmt.
    def exitYield_stmt(self, ctx:GrammarPyParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#raise_stmt.
    def enterRaise_stmt(self, ctx:GrammarPyParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#raise_stmt.
    def exitRaise_stmt(self, ctx:GrammarPyParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#import_stmt.
    def enterImport_stmt(self, ctx:GrammarPyParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#import_stmt.
    def exitImport_stmt(self, ctx:GrammarPyParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#import_name.
    def enterImport_name(self, ctx:GrammarPyParser.Import_nameContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#import_name.
    def exitImport_name(self, ctx:GrammarPyParser.Import_nameContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#import_from.
    def enterImport_from(self, ctx:GrammarPyParser.Import_fromContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#import_from.
    def exitImport_from(self, ctx:GrammarPyParser.Import_fromContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#import_as_name.
    def enterImport_as_name(self, ctx:GrammarPyParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#import_as_name.
    def exitImport_as_name(self, ctx:GrammarPyParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:GrammarPyParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:GrammarPyParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#import_as_names.
    def enterImport_as_names(self, ctx:GrammarPyParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#import_as_names.
    def exitImport_as_names(self, ctx:GrammarPyParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:GrammarPyParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:GrammarPyParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#dotted_name.
    def enterDotted_name(self, ctx:GrammarPyParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#dotted_name.
    def exitDotted_name(self, ctx:GrammarPyParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#global_stmt.
    def enterGlobal_stmt(self, ctx:GrammarPyParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#global_stmt.
    def exitGlobal_stmt(self, ctx:GrammarPyParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:GrammarPyParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:GrammarPyParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#assert_stmt.
    def enterAssert_stmt(self, ctx:GrammarPyParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#assert_stmt.
    def exitAssert_stmt(self, ctx:GrammarPyParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#compound_stmt.
    def enterCompound_stmt(self, ctx:GrammarPyParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#compound_stmt.
    def exitCompound_stmt(self, ctx:GrammarPyParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#if_stmt.
    def enterIf_stmt(self, ctx:GrammarPyParser.If_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#if_stmt.
    def exitIf_stmt(self, ctx:GrammarPyParser.If_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#while_stmt.
    def enterWhile_stmt(self, ctx:GrammarPyParser.While_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#while_stmt.
    def exitWhile_stmt(self, ctx:GrammarPyParser.While_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#for_stmt.
    def enterFor_stmt(self, ctx:GrammarPyParser.For_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#for_stmt.
    def exitFor_stmt(self, ctx:GrammarPyParser.For_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#try_stmt.
    def enterTry_stmt(self, ctx:GrammarPyParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#try_stmt.
    def exitTry_stmt(self, ctx:GrammarPyParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#with_stmt.
    def enterWith_stmt(self, ctx:GrammarPyParser.With_stmtContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#with_stmt.
    def exitWith_stmt(self, ctx:GrammarPyParser.With_stmtContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#with_item.
    def enterWith_item(self, ctx:GrammarPyParser.With_itemContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#with_item.
    def exitWith_item(self, ctx:GrammarPyParser.With_itemContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#except_clause.
    def enterExcept_clause(self, ctx:GrammarPyParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#except_clause.
    def exitExcept_clause(self, ctx:GrammarPyParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#suite.
    def enterSuite(self, ctx:GrammarPyParser.SuiteContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#suite.
    def exitSuite(self, ctx:GrammarPyParser.SuiteContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#test.
    def enterTest(self, ctx:GrammarPyParser.TestContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#test.
    def exitTest(self, ctx:GrammarPyParser.TestContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#test_nocond.
    def enterTest_nocond(self, ctx:GrammarPyParser.Test_nocondContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#test_nocond.
    def exitTest_nocond(self, ctx:GrammarPyParser.Test_nocondContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#lambdef.
    def enterLambdef(self, ctx:GrammarPyParser.LambdefContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#lambdef.
    def exitLambdef(self, ctx:GrammarPyParser.LambdefContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#lambdef_nocond.
    def enterLambdef_nocond(self, ctx:GrammarPyParser.Lambdef_nocondContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#lambdef_nocond.
    def exitLambdef_nocond(self, ctx:GrammarPyParser.Lambdef_nocondContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#or_test.
    def enterOr_test(self, ctx:GrammarPyParser.Or_testContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#or_test.
    def exitOr_test(self, ctx:GrammarPyParser.Or_testContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#and_test.
    def enterAnd_test(self, ctx:GrammarPyParser.And_testContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#and_test.
    def exitAnd_test(self, ctx:GrammarPyParser.And_testContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#not_test.
    def enterNot_test(self, ctx:GrammarPyParser.Not_testContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#not_test.
    def exitNot_test(self, ctx:GrammarPyParser.Not_testContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#comparison.
    def enterComparison(self, ctx:GrammarPyParser.ComparisonContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#comparison.
    def exitComparison(self, ctx:GrammarPyParser.ComparisonContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#comp_op.
    def enterComp_op(self, ctx:GrammarPyParser.Comp_opContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#comp_op.
    def exitComp_op(self, ctx:GrammarPyParser.Comp_opContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#star_expr.
    def enterStar_expr(self, ctx:GrammarPyParser.Star_exprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#star_expr.
    def exitStar_expr(self, ctx:GrammarPyParser.Star_exprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#expr.
    def enterExpr(self, ctx:GrammarPyParser.ExprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#expr.
    def exitExpr(self, ctx:GrammarPyParser.ExprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#xor_expr.
    def enterXor_expr(self, ctx:GrammarPyParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#xor_expr.
    def exitXor_expr(self, ctx:GrammarPyParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#and_expr.
    def enterAnd_expr(self, ctx:GrammarPyParser.And_exprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#and_expr.
    def exitAnd_expr(self, ctx:GrammarPyParser.And_exprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#shift_expr.
    def enterShift_expr(self, ctx:GrammarPyParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#shift_expr.
    def exitShift_expr(self, ctx:GrammarPyParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#arith_expr.
    def enterArith_expr(self, ctx:GrammarPyParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#arith_expr.
    def exitArith_expr(self, ctx:GrammarPyParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#term.
    def enterTerm(self, ctx:GrammarPyParser.TermContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#term.
    def exitTerm(self, ctx:GrammarPyParser.TermContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#factor.
    def enterFactor(self, ctx:GrammarPyParser.FactorContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#factor.
    def exitFactor(self, ctx:GrammarPyParser.FactorContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#power.
    def enterPower(self, ctx:GrammarPyParser.PowerContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#power.
    def exitPower(self, ctx:GrammarPyParser.PowerContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#atom.
    def enterAtom(self, ctx:GrammarPyParser.AtomContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#atom.
    def exitAtom(self, ctx:GrammarPyParser.AtomContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#testlist_comp.
    def enterTestlist_comp(self, ctx:GrammarPyParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#testlist_comp.
    def exitTestlist_comp(self, ctx:GrammarPyParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#trailer.
    def enterTrailer(self, ctx:GrammarPyParser.TrailerContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#trailer.
    def exitTrailer(self, ctx:GrammarPyParser.TrailerContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#subscriptlist.
    def enterSubscriptlist(self, ctx:GrammarPyParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#subscriptlist.
    def exitSubscriptlist(self, ctx:GrammarPyParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#subscript.
    def enterSubscript(self, ctx:GrammarPyParser.SubscriptContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#subscript.
    def exitSubscript(self, ctx:GrammarPyParser.SubscriptContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#sliceop.
    def enterSliceop(self, ctx:GrammarPyParser.SliceopContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#sliceop.
    def exitSliceop(self, ctx:GrammarPyParser.SliceopContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#exprlist.
    def enterExprlist(self, ctx:GrammarPyParser.ExprlistContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#exprlist.
    def exitExprlist(self, ctx:GrammarPyParser.ExprlistContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#testlist.
    def enterTestlist(self, ctx:GrammarPyParser.TestlistContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#testlist.
    def exitTestlist(self, ctx:GrammarPyParser.TestlistContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:GrammarPyParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:GrammarPyParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#classdef.
    def enterClassdef(self, ctx:GrammarPyParser.ClassdefContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#classdef.
    def exitClassdef(self, ctx:GrammarPyParser.ClassdefContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#arglist.
    def enterArglist(self, ctx:GrammarPyParser.ArglistContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#arglist.
    def exitArglist(self, ctx:GrammarPyParser.ArglistContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#argument.
    def enterArgument(self, ctx:GrammarPyParser.ArgumentContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#argument.
    def exitArgument(self, ctx:GrammarPyParser.ArgumentContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#comp_iter.
    def enterComp_iter(self, ctx:GrammarPyParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#comp_iter.
    def exitComp_iter(self, ctx:GrammarPyParser.Comp_iterContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#comp_for.
    def enterComp_for(self, ctx:GrammarPyParser.Comp_forContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#comp_for.
    def exitComp_for(self, ctx:GrammarPyParser.Comp_forContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#comp_if.
    def enterComp_if(self, ctx:GrammarPyParser.Comp_ifContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#comp_if.
    def exitComp_if(self, ctx:GrammarPyParser.Comp_ifContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#yield_expr.
    def enterYield_expr(self, ctx:GrammarPyParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#yield_expr.
    def exitYield_expr(self, ctx:GrammarPyParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#yield_arg.
    def enterYield_arg(self, ctx:GrammarPyParser.Yield_argContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#yield_arg.
    def exitYield_arg(self, ctx:GrammarPyParser.Yield_argContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#string.
    def enterString(self, ctx:GrammarPyParser.StringContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#string.
    def exitString(self, ctx:GrammarPyParser.StringContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#number.
    def enterNumber(self, ctx:GrammarPyParser.NumberContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#number.
    def exitNumber(self, ctx:GrammarPyParser.NumberContext):
        pass


    # Enter a parse tree produced by GrammarPyParser#integer.
    def enterInteger(self, ctx:GrammarPyParser.IntegerContext):
        pass

    # Exit a parse tree produced by GrammarPyParser#integer.
    def exitInteger(self, ctx:GrammarPyParser.IntegerContext):
        pass


