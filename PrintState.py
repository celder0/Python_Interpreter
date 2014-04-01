from State import  Statement

class PrintStatement(Statement):

    def __init__(self, expr):
        if (expr == None):
            raise ValueError("Null Expression ")
        self.expr = expr

    def execute(self):
        print (self.expr.evaluate())