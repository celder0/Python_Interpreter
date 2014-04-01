class LexException(Exception):
    def LexException(self,message,rowNumber,columnNumber):
        super
        if (message == None):
            raise ValueError("null string argument")
        if (rowNumber <= 0):
            raise ValueError("invalid row number argument")
        if (columnNumber <= 0):
            raise ValueError("invalid column number argument")

        self.rowNumber = rowNumber
        self.columnNumber = columnNumber

    def getRowNumber(self):
        return self.rowNumber

    def getColumnNumber(self):
        return self.columnNumber