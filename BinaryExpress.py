from Express import Expression
from TokenTypes import TokenType

class BinaryExpression(Expression):

    def __init__(self, op, expr1, expr2):
        if(op == None):
            raise ValueError("Null Arithmetic Operator Argument")
        self.op = op
        if(expr1 == None or expr2 == None):
            raise  ValueError("Null Expression Argument")
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if (self.op == TokenType.ADD_OP):
            return self.expr1.evaluate() + self.expr2.evaluate()
        elif (self.op == TokenType.SUB_OP):
            return self.expr1.evaluate() - self.expr2.evaluate()
        elif (self.op == TokenType.MULT_OP):
            return self.expr1.evaluate() * self.expr2.evaluate()
        elif (self.op == TokenType.DIV_OP):
            return self.expr1.evaluate() / self.expr2.evaluate()