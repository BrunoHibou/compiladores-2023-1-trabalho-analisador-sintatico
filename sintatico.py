from lexico import analisador_lexico


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1
        self.advance()

    def advance(self):
        print(f"Index = {self.token_index} e Current Token = {self.current_token}")
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None
        print(f"Index = {self.token_index} e Current Token = {self.current_token}")

    def match(self, expected_token):
        print(f"Current = {self.current_token}")
        print(f"Expected = {expected_token}")
        if self.current_token == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Expected '{expected_token}', but found '{self.current_token}'.")
        '''
                if self.current_token == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Expected '{expected_token}', but found '{self.current_token}'.")
        '''

    def parse(self):
        self.program()

        if self.current_token is not None:
            raise SyntaxError(f"Unexpected token '{self.current_token}' at the end of the program.")

    def program(self):
        while self.current_token is not None:
            self.declaration()

    def declaration(self):
        if self.current_token == "fun":
            self.funDecl()
        elif self.current_token == "var":
            self.varDecl()
        else:
            self.statement()

    def funDecl(self):
        self.match("fun")
        self.function()

    def varDecl(self):
        self.match("var")
        self.match("IDENTIFIER")
        if self.current_token in ["IDENTIFIER", "="]:
            self.match("=")
            self.expression()
        self.match(";")

    def statement(self):
        if self.current_token == "exprStmt":
            self.exprStmt()
        elif self.current_token == "for":
            self.forStmt()
        elif self.current_token == "if":
            self.ifStmt()
        elif self.current_token == "print":
            self.printStmt()
        elif self.current_token == "return":
            self.returnStmt()
        elif self.current_token == "while":
            self.whileStmt()
        elif self.current_token == "{":
            self.block()
        else:
            raise SyntaxError(f"Unexpected token '{self.current_token}' in statement.")

    def exprStmt(self):
        self.expression()
        self.match(";")

    def forStmt(self):
        self.match("for")
        self.match("(")
        if self.current_token == "var":
            self.varDecl()
        elif self.current_token == "exprStmt":
            self.exprStmt()
        elif self.current_token != ";":
            self.expression()
        self.match(";")
        if self.current_token != ";":
            self.expression()
        self.match(";")
        if self.current_token != ")":
            self.expression()
        self.match(")")
        self.statement()

    def ifStmt(self):
        self.match("if")
        self.match("(")
        self.expression()
        self.match(")")
        self.statement()
        if self.current_token == "else":
            self.match("else")
            self.statement()

    def printStmt(self):
        self.match("print")
        auxiliar = analisador_lexico(self.current_token)
        self.primary(auxiliar)
        self.match(";")

    def returnStmt(self):
        self.match("return")
        if self.current_token != ";":
            self.expression()
        self.match(";")

    def whileStmt(self):
        self.match("while")
        self.match("(")
        self.expression()
        self.match(")")
        self.statement()

    def block(self):
        self.match("{")
        while self.current_token != "}":
            self.declaration()
        self.match("}")

    def expression(self):
        self.assignment()

    def assignment(self):
        print(f"assignment = {self.current_token}")
        auxiliar = analisador_lexico(self.current_token)
        if auxiliar == "call" or auxiliar == "IDENTIFIER":
            self.call()
            if auxiliar == "=":
                self.match("=")
                self.assignment()

    def call(self):
        print(f"call = {self.current_token}")
        auxiliar = analisador_lexico(self.current_token)
        self.primary()
        if self.current_token == "(":
            self.match("(")
            if self.current_token != ")":
                self.arguments()
            self.match(")")
        elif self.current_token == ".":
            self.match(".")
            self.match("IDENTIFIER")

    def primary(self, auxiliar):
        if auxiliar in ["true", "false", "nil", "this", "NUMBER", "STRING", "IDENTIFIER"]:
            self.match(self.current_token)
        elif auxiliar == "(":
            self.match("(")
            self.expression()
            self.match(")")
        elif auxiliar == "super":
            self.match("super")
            self.match(".")
            self.match("IDENTIFIER")
        else:
            raise SyntaxError(f"Unexpected token '{self.current_token}', {auxiliar} in primary.")

    def function(self):
        self.match("IDENTIFIER")
        self.match("(")
        if self.current_token != ")":
            self.parameters()
        self.match(")")
        self.block()

    def parameters(self):
        self.match("IDENTIFIER")
        while self.current_token == ",":
            self.match(",")
            self.match("IDENTIFIER")

    def arguments(self):
        self.expression()
        while self.current_token == ",":
            self.match(",")
            self.expression()