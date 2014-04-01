class TokenType():

    INT_LIT, IDENT, ASSIGN_OP, ADD_OP, SUB_OP, MULT_OP, \
    DIV_OP, LE_OP, LT_OP, GE_OP, GT_OP, EQ_OP, NE_OP, IF, THEN, \
    ELSE, END, WHILE, DO, PUTS, UNTIL, DEF, EOS = range(23)

    def toString(self,value):
        tokens = ["INT_LIT", "IDENT", "ASSIGN_OP", "ADD_OP", "SUB_OP", "MULT_OP",
        "DIV_OP", "LE_OP", "LT_OP", "GE_OP", "GT_OP", "EQ_OP", "NE_OP", "IF", "THEN",
        "ELSE", "END", "WHILE", "DO", "PUTS", "UNTIL", "DEF", "EOS"]
        return tokens[value]
