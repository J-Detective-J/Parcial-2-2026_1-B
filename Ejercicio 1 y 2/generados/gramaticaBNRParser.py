# Generated from gramaticaBNR.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,154,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,64,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        72,8,4,1,5,1,5,1,5,1,5,1,5,3,5,79,8,5,1,6,1,6,1,6,1,6,5,6,85,8,6,
        10,6,12,6,88,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,99,8,8,
        10,8,12,8,102,9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,118,8,11,1,11,1,11,1,11,1,11,1,11,1,11,
        5,11,126,8,11,10,11,12,11,129,9,11,1,12,1,12,1,12,1,12,1,13,1,13,
        1,14,1,14,1,14,1,14,3,14,141,8,14,1,15,1,15,1,15,1,15,5,15,147,8,
        15,10,15,12,15,150,9,15,1,15,1,15,1,15,0,1,22,16,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,0,1,1,0,9,14,154,0,35,1,0,0,0,2,52,1,
        0,0,0,4,54,1,0,0,0,6,59,1,0,0,0,8,65,1,0,0,0,10,73,1,0,0,0,12,80,
        1,0,0,0,14,91,1,0,0,0,16,95,1,0,0,0,18,103,1,0,0,0,20,107,1,0,0,
        0,22,117,1,0,0,0,24,130,1,0,0,0,26,134,1,0,0,0,28,140,1,0,0,0,30,
        142,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,
        0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,
        1,0,0,0,40,41,3,4,2,0,41,42,5,1,0,0,42,53,1,0,0,0,43,44,3,6,3,0,
        44,45,5,1,0,0,45,53,1,0,0,0,46,47,3,8,4,0,47,48,5,1,0,0,48,53,1,
        0,0,0,49,50,3,10,5,0,50,51,5,1,0,0,51,53,1,0,0,0,52,40,1,0,0,0,52,
        43,1,0,0,0,52,46,1,0,0,0,52,49,1,0,0,0,53,3,1,0,0,0,54,55,5,17,0,
        0,55,56,5,18,0,0,56,57,5,28,0,0,57,58,3,12,6,0,58,5,1,0,0,0,59,60,
        5,19,0,0,60,63,5,28,0,0,61,62,5,20,0,0,62,64,3,20,10,0,63,61,1,0,
        0,0,63,64,1,0,0,0,64,7,1,0,0,0,65,66,5,21,0,0,66,67,5,28,0,0,67,
        68,5,22,0,0,68,71,3,16,8,0,69,70,5,20,0,0,70,72,3,20,10,0,71,69,
        1,0,0,0,71,72,1,0,0,0,72,9,1,0,0,0,73,74,5,23,0,0,74,75,5,24,0,0,
        75,78,5,28,0,0,76,77,5,20,0,0,77,79,3,20,10,0,78,76,1,0,0,0,78,79,
        1,0,0,0,79,11,1,0,0,0,80,81,5,2,0,0,81,86,3,14,7,0,82,83,5,3,0,0,
        83,85,3,14,7,0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,
        0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,90,5,4,0,0,90,13,1,0,0,0,91,
        92,5,28,0,0,92,93,5,5,0,0,93,94,3,28,14,0,94,15,1,0,0,0,95,100,3,
        18,9,0,96,97,5,3,0,0,97,99,3,18,9,0,98,96,1,0,0,0,99,102,1,0,0,0,
        100,98,1,0,0,0,100,101,1,0,0,0,101,17,1,0,0,0,102,100,1,0,0,0,103,
        104,5,28,0,0,104,105,5,6,0,0,105,106,3,28,14,0,106,19,1,0,0,0,107,
        108,3,22,11,0,108,21,1,0,0,0,109,110,6,11,-1,0,110,111,5,27,0,0,
        111,118,3,22,11,3,112,118,3,24,12,0,113,114,5,7,0,0,114,115,3,22,
        11,0,115,116,5,8,0,0,116,118,1,0,0,0,117,109,1,0,0,0,117,112,1,0,
        0,0,117,113,1,0,0,0,118,127,1,0,0,0,119,120,10,5,0,0,120,121,5,25,
        0,0,121,126,3,22,11,6,122,123,10,4,0,0,123,124,5,26,0,0,124,126,
        3,22,11,5,125,119,1,0,0,0,125,122,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,23,1,0,0,0,129,127,1,0,0,0,130,131,5,
        28,0,0,131,132,3,26,13,0,132,133,3,28,14,0,133,25,1,0,0,0,134,135,
        7,0,0,0,135,27,1,0,0,0,136,141,5,30,0,0,137,141,5,29,0,0,138,141,
        3,12,6,0,139,141,3,30,15,0,140,136,1,0,0,0,140,137,1,0,0,0,140,138,
        1,0,0,0,140,139,1,0,0,0,141,29,1,0,0,0,142,143,5,15,0,0,143,148,
        3,28,14,0,144,145,5,3,0,0,145,147,3,28,14,0,146,144,1,0,0,0,147,
        150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,
        148,1,0,0,0,151,152,5,16,0,0,152,31,1,0,0,0,12,35,52,63,71,78,86,
        100,117,125,127,140,148
    ]

class gramaticaBNRParser ( Parser ):

    grammarFileName = "gramaticaBNR.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "','", "'}'", "':'", "'='", 
                     "'('", "')'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'['", "']'", "'INSERT'", "'INTO'", "'FIND'", 
                     "'WHERE'", "'UPDATE'", "'SET'", "'DELETE'", "'FROM'", 
                     "'AND'", "'OR'", "'NOT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INSERT", "INTO", "FIND", "WHERE", "UPDATE", 
                      "SET", "DELETE", "FROM", "AND", "OR", "NOT", "ID", 
                      "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_insert = 2
    RULE_find = 3
    RULE_update = 4
    RULE_delete = 5
    RULE_document = 6
    RULE_pair = 7
    RULE_assignments = 8
    RULE_assignment = 9
    RULE_condition = 10
    RULE_expression = 11
    RULE_comparison = 12
    RULE_operator = 13
    RULE_value = 14
    RULE_array = 15

    ruleNames =  [ "program", "statement", "insert", "find", "update", "delete", 
                   "document", "pair", "assignments", "assignment", "condition", 
                   "expression", "comparison", "operator", "value", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    INSERT=17
    INTO=18
    FIND=19
    WHERE=20
    UPDATE=21
    SET=22
    DELETE=23
    FROM=24
    AND=25
    OR=26
    NOT=27
    ID=28
    NUMBER=29
    STRING=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaBNRParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaBNRParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaBNRParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramaticaBNRParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11141120) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(gramaticaBNRParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def insert(self):
            return self.getTypedRuleContext(gramaticaBNRParser.InsertContext,0)


        def find(self):
            return self.getTypedRuleContext(gramaticaBNRParser.FindContext,0)


        def update(self):
            return self.getTypedRuleContext(gramaticaBNRParser.UpdateContext,0)


        def delete(self):
            return self.getTypedRuleContext(gramaticaBNRParser.DeleteContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramaticaBNRParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.insert()
                self.state = 41
                self.match(gramaticaBNRParser.T__0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.find()
                self.state = 44
                self.match(gramaticaBNRParser.T__0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.update()
                self.state = 47
                self.match(gramaticaBNRParser.T__0)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.delete()
                self.state = 50
                self.match(gramaticaBNRParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(gramaticaBNRParser.INSERT, 0)

        def INTO(self):
            return self.getToken(gramaticaBNRParser.INTO, 0)

        def ID(self):
            return self.getToken(gramaticaBNRParser.ID, 0)

        def document(self):
            return self.getTypedRuleContext(gramaticaBNRParser.DocumentContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_insert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert" ):
                listener.enterInsert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert" ):
                listener.exitInsert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert" ):
                return visitor.visitInsert(self)
            else:
                return visitor.visitChildren(self)




    def insert(self):

        localctx = gramaticaBNRParser.InsertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_insert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(gramaticaBNRParser.INSERT)
            self.state = 55
            self.match(gramaticaBNRParser.INTO)
            self.state = 56
            self.match(gramaticaBNRParser.ID)
            self.state = 57
            self.document()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIND(self):
            return self.getToken(gramaticaBNRParser.FIND, 0)

        def ID(self):
            return self.getToken(gramaticaBNRParser.ID, 0)

        def WHERE(self):
            return self.getToken(gramaticaBNRParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ConditionContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_find

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFind" ):
                listener.enterFind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFind" ):
                listener.exitFind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFind" ):
                return visitor.visitFind(self)
            else:
                return visitor.visitChildren(self)




    def find(self):

        localctx = gramaticaBNRParser.FindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_find)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(gramaticaBNRParser.FIND)
            self.state = 60
            self.match(gramaticaBNRParser.ID)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 61
                self.match(gramaticaBNRParser.WHERE)
                self.state = 62
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(gramaticaBNRParser.UPDATE, 0)

        def ID(self):
            return self.getToken(gramaticaBNRParser.ID, 0)

        def SET(self):
            return self.getToken(gramaticaBNRParser.SET, 0)

        def assignments(self):
            return self.getTypedRuleContext(gramaticaBNRParser.AssignmentsContext,0)


        def WHERE(self):
            return self.getToken(gramaticaBNRParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ConditionContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_update

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate" ):
                listener.enterUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate" ):
                listener.exitUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = gramaticaBNRParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_update)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(gramaticaBNRParser.UPDATE)
            self.state = 66
            self.match(gramaticaBNRParser.ID)
            self.state = 67
            self.match(gramaticaBNRParser.SET)
            self.state = 68
            self.assignments()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 69
                self.match(gramaticaBNRParser.WHERE)
                self.state = 70
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(gramaticaBNRParser.DELETE, 0)

        def FROM(self):
            return self.getToken(gramaticaBNRParser.FROM, 0)

        def ID(self):
            return self.getToken(gramaticaBNRParser.ID, 0)

        def WHERE(self):
            return self.getToken(gramaticaBNRParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ConditionContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete" ):
                return visitor.visitDelete(self)
            else:
                return visitor.visitChildren(self)




    def delete(self):

        localctx = gramaticaBNRParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_delete)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(gramaticaBNRParser.DELETE)
            self.state = 74
            self.match(gramaticaBNRParser.FROM)
            self.state = 75
            self.match(gramaticaBNRParser.ID)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 76
                self.match(gramaticaBNRParser.WHERE)
                self.state = 77
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaBNRParser.PairContext)
            else:
                return self.getTypedRuleContext(gramaticaBNRParser.PairContext,i)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = gramaticaBNRParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(gramaticaBNRParser.T__1)
            self.state = 81
            self.pair()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 82
                self.match(gramaticaBNRParser.T__2)
                self.state = 83
                self.pair()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(gramaticaBNRParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaBNRParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ValueContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = gramaticaBNRParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(gramaticaBNRParser.ID)
            self.state = 92
            self.match(gramaticaBNRParser.T__4)
            self.state = 93
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaBNRParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(gramaticaBNRParser.AssignmentContext,i)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_assignments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignments" ):
                listener.enterAssignments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignments" ):
                listener.exitAssignments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignments" ):
                return visitor.visitAssignments(self)
            else:
                return visitor.visitChildren(self)




    def assignments(self):

        localctx = gramaticaBNRParser.AssignmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.assignment()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 96
                self.match(gramaticaBNRParser.T__2)
                self.state = 97
                self.assignment()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaBNRParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ValueContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramaticaBNRParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(gramaticaBNRParser.ID)
            self.state = 104
            self.match(gramaticaBNRParser.T__5)
            self.state = 105
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = gramaticaBNRParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(gramaticaBNRParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaBNRParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaBNRParser.ExpressionContext,i)


        def comparison(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ComparisonContext,0)


        def AND(self):
            return self.getToken(gramaticaBNRParser.AND, 0)

        def OR(self):
            return self.getToken(gramaticaBNRParser.OR, 0)

        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaBNRParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 110
                self.match(gramaticaBNRParser.NOT)
                self.state = 111
                self.expression(3)
                pass
            elif token in [28]:
                self.state = 112
                self.comparison()
                pass
            elif token in [7]:
                self.state = 113
                self.match(gramaticaBNRParser.T__6)
                self.state = 114
                self.expression(0)
                self.state = 115
                self.match(gramaticaBNRParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 125
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaBNRParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 120
                        self.match(gramaticaBNRParser.AND)
                        self.state = 121
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaBNRParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 123
                        self.match(gramaticaBNRParser.OR)
                        self.state = 124
                        self.expression(5)
                        pass

             
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaBNRParser.ID, 0)

        def operator(self):
            return self.getTypedRuleContext(gramaticaBNRParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ValueContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = gramaticaBNRParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(gramaticaBNRParser.ID)
            self.state = 131
            self.operator()
            self.state = 132
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = gramaticaBNRParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramaticaBNRParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(gramaticaBNRParser.NUMBER, 0)

        def document(self):
            return self.getTypedRuleContext(gramaticaBNRParser.DocumentContext,0)


        def array(self):
            return self.getTypedRuleContext(gramaticaBNRParser.ArrayContext,0)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = gramaticaBNRParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_value)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(gramaticaBNRParser.STRING)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(gramaticaBNRParser.NUMBER)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.document()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaBNRParser.ValueContext)
            else:
                return self.getTypedRuleContext(gramaticaBNRParser.ValueContext,i)


        def getRuleIndex(self):
            return gramaticaBNRParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = gramaticaBNRParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(gramaticaBNRParser.T__14)
            self.state = 143
            self.value()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 144
                self.match(gramaticaBNRParser.T__2)
                self.state = 145
                self.value()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(gramaticaBNRParser.T__15)
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
        self._predicates[11] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




