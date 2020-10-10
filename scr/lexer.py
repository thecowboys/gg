import re



class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):

        # Where all the Tokens created by lexer will be stored
        tokens = []

        # Create a word list of the source code
        source_code = self.source_code.split()

        # This will keep track of the word index we are in the source code
        source_index = 0

        # Loop through each word in source code to generate tokens
        while source_index < len(source_code):

            word = source_code[source_index]

            # This will recognise a variable and create a token for it
            if word == "var": tokens.append(["VAR_DECLERATION", word])

            # print
            elif word == "print": tokens.append(["PRINT_DECLERATION", word])

            # This will recognise a word and create an identifier token for it
            elif re.match("[a-z]", word) or re.match("[A-Z]", word):
                tokens.append(["IDENTIFIER", word])

            # string type
            elif word.startswith("'") and word.endswith("'") or word.startswith('"') and word.endswith('"'):
                tokens.append(["STRING", word])

            # This will recognise a intiger and create an integer token for it
            elif re.match("[0-9]", word):
                tokens.append(["INTEGER", word])

            # This will recognise a operators and create an operator token for it
            elif word is "=" or "/" or "*" or "-" or "+":
                tokens.append(["OPERATOR", word])

            # Increases word index after checking it
            source_index += 1

        print(tokens)

        # Return created tokens
        return tokens
