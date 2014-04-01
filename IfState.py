from State import Statement


class IfStatement(Statement):

    def __init__(self, expr, cb1, cb2):
        if (expr == None):
            raise ValueError("Null Boolean Expression Argument")
        if (cb1 == None or cb2 == None):
            raise ValueError("Null Code Block Argument")
        self.expr = expr
        self.cb1 = cb1
        self.cb2 = cb2

    def execute(self):
        if (self.expr.evaluate()):
            self.cb1.execute()
        else:
            self.cb2.execute()