
class ParserException(Exception):
    def ParserException(self,message):
        if(message == None):
            raise ValueError("Null String Argument")