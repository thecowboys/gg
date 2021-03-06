import lexer as lexer
import parser as parser

def main():

    # Read the current flow source code in test.gg and store it in variable
    content = ""
    with open("test.gg", "r") as file:
        content = file.read()

    #
    # Lexer
    #

    # We call the lexer class and initalise it with the source code
    lex = lexer.Lexer(content)
    # We now call the tokenize method
    tokens = lex.tokenize()

    #
    # Parser
    #

    parse = parser.Parser(tokens)
    parse.parse()

main()
