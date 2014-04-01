from TokenTypes import TokenType

class BooleanExpression:

    def __init__(self,op,expr1,expr2):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        result = True
        if (self.op == TokenType.EQ_OP):
            result = self.expr1.evaluate() == self.expr2.evaluate()
        elif (self.op == TokenType.NE_OP):
            result = self.expr1.evaluate() != self.expr2.evaluate()
        elif (self.op == TokenType.LT_OP):
            result = self.expr1.evaluate() < self.expr2.evaluate()
        elif (self.op == TokenType.LE_OP):
            result = self.expr1.evaluate() <= self.expr2.evaluate()
        elif (self.op == TokenType.GT_OP):
            result = self.expr1.evaluate() > self.expr2.evaluate()
        elif (self.op == TokenType.GE_OP):
            result = self.expr1.evaluate() >= self.expr2.evaluate()
        return result