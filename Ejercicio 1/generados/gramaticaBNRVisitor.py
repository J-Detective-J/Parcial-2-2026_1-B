# Generated from gramaticaBNR.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaBNRParser import gramaticaBNRParser
else:
    from gramaticaBNRParser import gramaticaBNRParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaBNRParser.

class gramaticaBNRVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaBNRParser#program.
    def visitProgram(self, ctx:gramaticaBNRParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#statement.
    def visitStatement(self, ctx:gramaticaBNRParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#insert.
    def visitInsert(self, ctx:gramaticaBNRParser.InsertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#find.
    def visitFind(self, ctx:gramaticaBNRParser.FindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#update.
    def visitUpdate(self, ctx:gramaticaBNRParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#delete.
    def visitDelete(self, ctx:gramaticaBNRParser.DeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#document.
    def visitDocument(self, ctx:gramaticaBNRParser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#pair.
    def visitPair(self, ctx:gramaticaBNRParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#assignments.
    def visitAssignments(self, ctx:gramaticaBNRParser.AssignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#assignment.
    def visitAssignment(self, ctx:gramaticaBNRParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#condition.
    def visitCondition(self, ctx:gramaticaBNRParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#expression.
    def visitExpression(self, ctx:gramaticaBNRParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#comparison.
    def visitComparison(self, ctx:gramaticaBNRParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#operator.
    def visitOperator(self, ctx:gramaticaBNRParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#value.
    def visitValue(self, ctx:gramaticaBNRParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaBNRParser#array.
    def visitArray(self, ctx:gramaticaBNRParser.ArrayContext):
        return self.visitChildren(ctx)



del gramaticaBNRParser