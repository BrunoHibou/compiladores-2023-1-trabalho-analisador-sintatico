from lexico import analisador_lexico
import sys


def parse(tokens):
    current_token = None
    auxiliar = None
    token_index = 0

    def advance():
        nonlocal current_token, token_index, auxiliar
        if token_index < len(tokens):
            current_token = tokens[token_index]
            auxiliar = analisador_lexico(current_token)
            token_index += 1
        else:
            current_token = None

    def match(expected_token):
        nonlocal current_token, auxiliar
        if auxiliar == expected_token:
            advance()
        else:
            print(f"--- SyntaxError: Expected '{expected_token}', but found '{current_token}'. ---")
            sys.exit()

    def program():
        while current_token is not None:
            declaration()

    def declaration():
        if current_token == "fun":
            funDecl()
        elif current_token == "var":
            varDecl()
        else:
            statement()

    def funDecl():
        match("fun")
        function()

    def function():
        match("IDENTIFIER")
        match("(")
        if current_token != ")":
            parameters()
        match(")")
        block()

    def parameters():
        match("IDENTIFIER")
        while current_token == ",":
            match(",")
            match("IDENTIFIER")

    def block():
        match("{")
        while current_token != "}":
            declaration()
        match("}")

    def varDecl():
        match("var")
        match("IDENTIFIER")
        if current_token == "=":
            match("=")
            expression()
        match(";")

    def statement():
        nonlocal auxiliar
        if auxiliar == "IDENTIFIER":
            exprStmt()
        elif current_token == "for":
            forStmt()
        elif current_token == "if":
            ifStmt()
        elif current_token == "print":
            printStmt()
        elif current_token == "return":
            returnStmt()
        elif current_token == "while":
            whileStmt()
        elif current_token == "{":
            block()
        else:
            print(f"--- SyntaxError: Unexpected token '{current_token}' in statement. ---")
            sys.exit()

    def exprStmt():
        expression()
        match(";")

    def forStmt():
        match("for")
        match("(")
        if current_token == "var":
            varDecl()
        elif current_token == "exprStmt":
            exprStmt()
        elif current_token != ";":
            expression()
        match(";")
        if current_token != ";":
            expression()
        match(";")
        if current_token != ")":
            expression()
        match(")")
        statement()

    def ifStmt():
        match("if")
        match("(")
        expression()
        match(")")
        statement()
        if current_token == "else":
            match("else")
            statement()

    def printStmt():
        match("print")
        expression()
        match(";")

    def returnStmt():
        match("return")
        if current_token != ";":
            expression()
        match(";")

    def whileStmt():
        match("while")
        match("(")
        expression()
        match(")")
        statement()

    def expression():
        assignment()

    def assignment():
        print("yey") #o erro tá aqui em algum lugar
        nonlocal auxiliar
        if auxiliar == "IDENTIFIER":
            match("IDENTIFIER")
            if current_token == "=":
                match("=")
                assignment()
            else:
                logic_or()
        else:
            logic_or()

    def logic_or():
        logic_and()
        while current_token == "or":
            match("or")
            logic_and()

    def logic_and():
        equality()
        while current_token == "and":
            match("and")
            equality()

    def equality():
        comparison()
        while current_token in ["!=", "=="]:
            match(current_token)
            comparison()

    def comparison():
        term()
        while current_token in [">", ">=", "<", "<="]:
            match(current_token)
            term()

    def term():
        factor()
        while current_token in ["-", "+"]:
            match(current_token)
            factor()

    def factor():
        unary()
        while current_token in ["/", "*"]:
            match(current_token)
            unary()

    def unary():
        if current_token in ["!", "-"]:
            match(current_token)
            unary()
        else:
            call()

    def call():
        primary()
        while current_token in ["(", "."]:
            if current_token == "(":
                match("(")
                if current_token != ")":
                    arguments()
                match(")")
            elif current_token == ".":
                match(".")
                match("IDENTIFIER")

    def primary():
        nonlocal auxiliar
        if auxiliar in ["true", "false", "nil", "this", "NUMBER", "STRING", "IDENTIFIER"]:
            match(auxiliar)
        elif auxiliar == "(":
            match("(")
            expression()
            match(")")
        elif auxiliar == "super":
            match("super")
            match(".")
            match("IDENTIFIER")
        '''else:
            print(f"--- SyntaxError: Unexpected token '{current_token}' in primary. ---")
            sys.exit()'''

    def arguments():
        expression()
        while current_token == ",":
            match(",")
            expression()

    advance()
    program()

    if current_token is not None:
        print(f"--- SyntaxError: Unexpected token '{current_token}' at the end of the program. ---")
        sys.exit()
    else:
        print("----------------- Análise Sintática Concluída com Sucesso -----------------")