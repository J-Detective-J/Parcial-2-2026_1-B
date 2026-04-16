# Generated from gramaticaBNR.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaBNRParser import gramaticaBNRParser
else:
    from gramaticaBNRParser import gramaticaBNRParser

# This class defines a complete listener for a parse tree produced by gramaticaBNRParser.
class gramaticaBNRListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaBNRParser#program.
    def enterProgram(self, ctx:gramaticaBNRParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#program.
    def exitProgram(self, ctx:gramaticaBNRParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#statement.
    def enterStatement(self, ctx:gramaticaBNRParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#statement.
    def exitStatement(self, ctx:gramaticaBNRParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#insert.
    def enterInsert(self, ctx:gramaticaBNRParser.InsertContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#insert.
    def exitInsert(self, ctx:gramaticaBNRParser.InsertContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#find.
    def enterFind(self, ctx:gramaticaBNRParser.FindContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#find.
    def exitFind(self, ctx:gramaticaBNRParser.FindContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#update.
    def enterUpdate(self, ctx:gramaticaBNRParser.UpdateContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#update.
    def exitUpdate(self, ctx:gramaticaBNRParser.UpdateContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#delete.
    def enterDelete(self, ctx:gramaticaBNRParser.DeleteContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#delete.
    def exitDelete(self, ctx:gramaticaBNRParser.DeleteContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#document.
    def enterDocument(self, ctx:gramaticaBNRParser.DocumentContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#document.
    def exitDocument(self, ctx:gramaticaBNRParser.DocumentContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#pair.
    def enterPair(self, ctx:gramaticaBNRParser.PairContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#pair.
    def exitPair(self, ctx:gramaticaBNRParser.PairContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#assignments.
    def enterAssignments(self, ctx:gramaticaBNRParser.AssignmentsContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#assignments.
    def exitAssignments(self, ctx:gramaticaBNRParser.AssignmentsContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#assignment.
    def enterAssignment(self, ctx:gramaticaBNRParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#assignment.
    def exitAssignment(self, ctx:gramaticaBNRParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#condition.
    def enterCondition(self, ctx:gramaticaBNRParser.ConditionContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#condition.
    def exitCondition(self, ctx:gramaticaBNRParser.ConditionContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#expression.
    def enterExpression(self, ctx:gramaticaBNRParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#expression.
    def exitExpression(self, ctx:gramaticaBNRParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#comparison.
    def enterComparison(self, ctx:gramaticaBNRParser.ComparisonContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#comparison.
    def exitComparison(self, ctx:gramaticaBNRParser.ComparisonContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#operator.
    def enterOperator(self, ctx:gramaticaBNRParser.OperatorContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#operator.
    def exitOperator(self, ctx:gramaticaBNRParser.OperatorContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#value.
    def enterValue(self, ctx:gramaticaBNRParser.ValueContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#value.
    def exitValue(self, ctx:gramaticaBNRParser.ValueContext):
        pass


    # Enter a parse tree produced by gramaticaBNRParser#array.
    def enterArray(self, ctx:gramaticaBNRParser.ArrayContext):
        pass

    # Exit a parse tree produced by gramaticaBNRParser#array.
    def exitArray(self, ctx:gramaticaBNRParser.ArrayContext):
        pass



del gramaticaBNRParser