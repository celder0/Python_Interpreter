from TokenTypes import TokenType

class Token(object):

    def __init__(self,tok,lexeme,lineNum,columnNum):
        self.tok = tok
        self.lexeme = lexeme
        if (lineNum <= 0):
            raise  ValueError("invalid line number")
        self.lineNum = lineNum
        if (columnNum <= 0):
            raise ValueError("invalid column number")
        self.columnNum = columnNum
        self.contents = self.tok.__str__() + ": " + self.lexeme + " row: " + self.lineNum.__str__() + " column: " + self.columnNum.__str__()

    def getTokenType(self):
        return self.tok

    def getLexeme(self):
        return self.lexeme

    def getLineNumber(self):
        return self.lineNum

    def getColumnNumber(self):
        return self.columnNum

    def toString(self):
        return self.tok.__str__ + ": " + self.lexeme + "row: " + self.lineNum.__str__ + " column: " + self.columnNum.__str__