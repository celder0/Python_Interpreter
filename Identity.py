from UnaryExpress import UnaryExpression
from Mem import Memory

class Id(UnaryExpression):

    def __init__(self, ch):
        self.ch = ch

    def evaluate(self):
        return Memory.fetch(Memory,self.ch)

    def getCh(self):
        return self.ch

