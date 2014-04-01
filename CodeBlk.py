
class CodeBlock:

    def __init__(self):
        self.stmts = []

    def add(self,stmt):
        self.stmts.append(stmt)

    def execute(self):
        for i in range(0,len(self.stmts)):
            self.stmts[i].execute()