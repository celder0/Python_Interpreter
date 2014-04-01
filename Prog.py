

class Program:

    def __init__(self, cb):
        if (cb == None):
            raise ValueError("Null Code Block Exception")
        self.cb = cb

    def execute(self):
        self.cb.execute()