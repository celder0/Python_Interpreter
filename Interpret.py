from Par import Parser

if __name__ == '__main__':
    p = Parser("Test5.rb")
    prog = p.parse()
    prog.execute()
