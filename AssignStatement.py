from State import Statement
from Mem import Memory

class AssignmentStatement(Statement):

    def __init__(self, var, expr):
        if (var == None):
            raise ValueError("Null Id Argument")
        if (expr == None):
            raise ValueError("Null Expression Argument")
        self.var = var
        self.expr = expr

    def execute(self):
        ch  =   self.var.getCh()
        value = self.expr.evaluate()
        Memory.store(Memory,ch,value)

