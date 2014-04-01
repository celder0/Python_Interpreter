
from Tokens import Token
from TokenTypes import TokenType
from LexemeException import LexException

class LexicalAnalyzer():

    tokens = []

    def add_to_tokens(self,i):
        global tokens
        self.tokens.append(i)

    def __init__(self, fileName):
        if isinstance(fileName, str):
            lineNum = 0
            file = open(fileName)
            for line in file.readlines():
                lineNum = lineNum + 1
                self.processLine(line,lineNum)
            self.add_to_tokens(Token(TokenType.EOS, "EOS", lineNum + 1, 1))
        else:
            raise ValueError("File Name must be a string")

    def processLine(self, line, rowNum):
        index = 0
        done = False
        while not done:
            index = self.skipWhiteSpace(line,index)
            if(index == len(line)):
                done = True;
            else:
                columnNum = index + 1
                lexeme = self.getLexeme(line,index)
                index = index + len(lexeme)
                tok = self.getTokenType(lexeme)
                if (tok == None):
                    raise LexException("invalid lexeme", rowNum, columnNum)
                t = Token(tok,lexeme,rowNum,columnNum);
                self.add_to_tokens(t)


    def getLexeme(self,line,index):
        if(line[index].isalpha()):
            i = index
            while (i < len(line) and (line[i].isalpha() or line[i].isdigit())):
                i = i + 1
                lexeme = line[index:i]
        elif(line[index].isdigit()):
            i = index
            while(i<len(line) and line[i].isdigit()):
                i = i + 1
                lexeme = line[index:i]
        else:
            i = index
            while (i < len(line) and not line[i].isspace()):
                i = i + 1
                lexeme = line[index:i]
        return lexeme


    def getTokenType(self,lexeme):
        tok = None
        if(lexeme[0].isalpha()):
            if(len(lexeme) > 1):
                if(lexeme == "def"):
                    tok = TokenType.DEF
                elif(lexeme == "if"):
                    tok = TokenType.IF
                elif(lexeme == "then"):
                    tok = TokenType.THEN
                elif(lexeme == "else"):
                    tok = TokenType.ELSE
                elif(lexeme == "end"):
                    tok = TokenType.END
                elif(lexeme == "while"):
                    tok = TokenType.WHILE
                elif(lexeme == "do"):
                    tok = TokenType.DO
                elif(lexeme == "puts"):
                    tok = TokenType.PUTS
                elif(lexeme == "until"):
                    tok = TokenType.UNTIL
            else:
                tok = TokenType.IDENT
        elif(lexeme[0].isdigit()):
            tok = TokenType.INT_LIT
        else:
            if (len(lexeme) <= 2):
                if (lexeme == "+"):
                    tok = TokenType.ADD_OP
                elif (lexeme == "-"):
                    tok = TokenType.SUB_OP
                elif (lexeme == "*"):
                    tok = TokenType.MULT_OP
                elif (lexeme == "/"):
                    tok = TokenType.DIV_OP
                elif (lexeme == "/="):
                    tok = TokenType.NE_OP
                elif (lexeme == "="):
                    tok = TokenType.ASSIGN_OP
                elif (lexeme == "=="):
                    tok = TokenType.EQ_OP
                elif (lexeme == "<"):
                    tok = TokenType.LT_OP
                elif (lexeme == "<="):
                    tok = TokenType.LE_OP
                elif (lexeme == ">"):
                    tok = TokenType.GT_OP
                elif (lexeme == ">="):
                    tok = TokenType.GE_OP
        return tok


    def skipWhiteSpace(self, line, index):
        while (index < len(line) and line[index].isspace()):
            index = index + 1
        return index

    def getNextToken(self):
        global tokens
        return self.tokens.pop(0)

    def getLookAheadToken(self):
        global tokens
        return self.tokens[0]

    def moreTokens(self):
        global tokens
        return not (len(self.tokens) == 0)