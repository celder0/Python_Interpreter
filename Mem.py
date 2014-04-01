
class Memory:

    global mem
    mem = [0 for i in range(52)]



    def fetch(self, ch):
        index = self.getIndex(self,ch)
        return mem[index]

    def store(self,ch,value):
        index = self.getIndex(self,ch)
        mem[index] = value

    def getIndex(self, ch):
        a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        return a.index(ch)