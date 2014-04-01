from LexAnalyzer import LexicalAnalyzer
from LexemeException import LexException

if __name__ == '__main__':
    try:

        lex = LexicalAnalyzer("Test1.rb");
        while (lex.moreTokens()):
            print(lex.getNextToken().contents)
    except LexException as e:
        print(e.message)
    except ValueError as e:
        print(e.message)
    except Exception as e:
        print(e.message)
