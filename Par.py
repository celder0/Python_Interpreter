from LexAnalyzer import LexicalAnalyzer
from TokenTypes import TokenType
from CodeBlk import CodeBlock
from AssignStatement import AssignmentStatement
from IfState import IfStatement
from PrintState import PrintStatement
from UntilState import UntilStatement
from WhileState import WhileStatement
from Identity import Id
from LitInt import LiteralInteger
from BinaryExpress import BinaryExpression
from BoolExpress import BooleanExpression
from Prog import Program
from ParseException import ParserException

class Parser:

    def __init__(self, fileName):
        self.lex = LexicalAnalyzer(fileName)

    def parse(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.DEF)
        cb = self.getCodeBlock()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.END)
        tok = self.lex.getNextToken()
        if (tok.getTokenType() != TokenType.EOS):
            raise ParserException("garbage at end of program")
        return Program(cb)

    def match(self,tok,type):
        if(tok.getTokenType() != type):
            raise ParserException(TokenType.toString(self,type) + " expected at row " + str(tok.getLineNumber()) + " and column " + str(tok.getColumnNumber()))

    def getCodeBlock(self):
        cb = CodeBlock()
        stmt = self.getStatement()
        cb.add(stmt)
        tok = self.lex.getLookAheadToken()
        while (self.isValidStartOfStatement(tok)):
            stmt = self.getStatement()
            cb.add(stmt)
            tok = self.lex.getLookAheadToken()
        return cb

    def isValidStartOfStatement(self,tok):
        return (tok.getTokenType() == TokenType.IF or tok.getTokenType() == TokenType.IDENT or
                tok.getTokenType() == TokenType.WHILE or tok.getTokenType() == TokenType.UNTIL or
                tok.getTokenType() == TokenType.PUTS)

    def getStatement(self):
        tok = self.lex.getLookAheadToken()
        if (tok.getTokenType() == TokenType.IDENT):
            stmt = self.getAssignmentStatement()
        elif (tok.getTokenType() == TokenType.IF):
            stmt = self.getIfStatement()
        elif (tok.getTokenType() == TokenType.PUTS):
            stmt = self.getPrintStatement()
        elif (tok.getTokenType() == TokenType.UNTIL):
            stmt = self.getUntilStatement()
        elif (tok.getTokenType() == TokenType.WHILE):
            stmt = self.getWhileStatement()
        else:
            raise ParserException("Statement Expected here")
        return stmt

    def getWhileStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.WHILE)
        expr = self.getBooleanExpression()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.DO)
        cb = self.getCodeBlock()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.END)
        return WhileStatement(expr,cb)

    def getUntilStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.UNTIL)
        expr = self.getBooleanExpression()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.DO)
        cb = self.getCodeBlock()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.END)
        return UntilStatement(expr,cb)

    def getPrintStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.PUTS)
        expr = self.getExpression()
        return PrintStatement(expr)


    def getIfStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.IF)
        expr = self.getBooleanExpression()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.THEN)
        cb1 = self.getCodeBlock()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.ELSE)
        cb2 = self.getCodeBlock()
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.END)
        return IfStatement(expr,cb1,cb2)


    def getAssignmentStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.IDENT)
        var = Id(tok.getLexeme()[0])
        tok = self.lex.getNextToken()
        self.match(tok,TokenType.ASSIGN_OP)
        expr = self.getExpression()
        return AssignmentStatement(var,expr)

    def getExpression(self):
        tok = self.lex.getLookAheadToken()
        if (tok.getTokenType() == TokenType.IDENT):
            tok = self.lex.getNextToken()
            value = tok.getLexeme()
            expr = Id(value[0])
        elif (tok.getTokenType() == TokenType.INT_LIT):
            tok = self.lex.getNextToken()
            value = tok.getLexeme()
            expr = LiteralInteger(int(value))
        else:
            op = self.getArithmeticOperator()
            expr1 = self.getExpression()
            expr2 = self.getExpression()
            expr = BinaryExpression(op,expr1,expr2)
        return expr

    def getArithmeticOperator(self):
        tok = self.lex.getNextToken()
        if (tok.getTokenType() == TokenType.ADD_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.SUB_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.MULT_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.DIV_OP):
            op = tok.getTokenType()
        else:
            raise ParserException("Arithmetic Operator expected at row " + str(tok.getRowNumber()) + " and column "
                             + str(tok.getColumnNumber()))
        return op

    def getBooleanExpression(self):
        op = self.getRelationalOperator()
        expr1 = self.getExpression()
        expr2 = self.getExpression()
        return BooleanExpression(op,expr1,expr2)

    def getRelationalOperator(self):
        tok = self.lex.getNextToken()
        if (tok.getTokenType() == TokenType.NE_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.EQ_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.LT_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.LE_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.GT_OP):
            op = tok.getTokenType()
        elif (tok.getTokenType() == TokenType.GE_OP):
            op = tok.getTokenType()
        else:
            raise ParserException("relational operator expected at row " + str(tok.getRowNumber()) + " and column "
                             + str(tok.getColumnNumber()))
        return op

