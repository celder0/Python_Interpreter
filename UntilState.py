from State import Statement

class UntilStatement(Statement):

    def __init__(self, expr, cb):
        if (expr == None):
            raise ValueError("Null Expression Argument")
        if (cb == None):
            raise ValueError("Null Code Block Argument")
        self.expr = expr
        self.cb = cb

    def execute(self):
        while (not self.expr.evaluate()):
            self.cb.execute()