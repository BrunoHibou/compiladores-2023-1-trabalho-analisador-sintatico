from dicionarios import *
import re
import sys


def analisador_lexico(tokens):
    for token in tokens:
        print(token)
        if encontrar_constantes_textuais(token):
            continue
        if encontrar_palavras_reservadas(token):
            continue
        if encontrar_operadores(token):
            continue
        if encontrar_numeros(token):
            continue
        if encontrar_delimitadores(token):
            continue
        if encontrar_identificadores(token):
            continue
        else:
            print(f"erro lexico {token}")
            sys.exit()


def encontrar_palavras_reservadas(programa):
    padrao = r"\b(" + "|".join(palavras_reservadas) + r")\b"
    palavras_reservadas_encontradas = re.findall(padrao, programa)
    return palavrasReservadas(palavras_reservadas_encontradas)


def palavrasReservadas(palavras_reservadas_encontradas):
    if not palavras_reservadas_encontradas:
        # print("Não há Palavras Reservadas.")
        return False
    for palavra in palavras_reservadas_encontradas:
        print(f"'{palavra}' é uma Palavra Reservada.")
        return True


def encontrar_operadores(programa):
    padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    operadores_encontrados = re.findall(padrao, programa)
    # nova_string = re.sub(padrao, lambda match: ' ', programa)
    return imprimir_operadores(operadores_encontrados)


def imprimir_operadores(operadores_encontrados):
    if not operadores_encontrados:
        # print("Não há Operadores.")
        return False
    for op in operadores_encontrados:
        print(f"'{op[1]}' é um Operador.")
        return True


def encontrar_numeros(programa):
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)
    inteiros = [num for num in numeros_encontrados if '.' not in num]
    floats = [num for num in numeros_encontrados if '.' in num]

    resposta = imprimir_numeros(inteiros, 'Inteiro')
    if resposta:
        return resposta
    else:
        resposta = imprimir_numeros(floats, 'Flutuante')

    # nova_string = re.sub(padrao, lambda match: ' ', programa)
    return resposta


def imprimir_numeros(numeros, tipo):
    if not numeros:
        # print(f"Não há nenhum numeral de tipo {tipo}.")
        return False
    for num in numeros:
        print(f"'{num}' é um numeral {tipo}.")
        return True


def encontrar_constantes_textuais(programa):
    padrao = expressoes_regulares['constantes_textuais']
    constantes_encontradas = re.findall(padrao, programa)
    return imprimir_constantes_textuais(constantes_encontradas)


def imprimir_constantes_textuais(constantes_encontradas):
    if not constantes_encontradas:
        # print("Não há Constantes Textuais.")
        return False
    for constante in constantes_encontradas:
        print(f"'{constante}' é uma Constante Textual.")
        return True


def encontrar_delimitadores(programa):
    padrao = expressoes_regulares['delimitadores']
    delimitadores_encontrados = re.findall(padrao, programa)
    # nova_string = re.sub(padrao, lambda match: ' ', programa)
    return imprimir_delimitadores(delimitadores_encontrados)


def imprimir_delimitadores(delimitadores_encontrados):
    if not delimitadores_encontrados:
        # print("Não há Delimitadores.")
        return False
    for caracteres in delimitadores_encontrados:
        print(f"'{caracteres}' é um Delimitador.")
        return True


def encontrar_identificadores(programa):
    padrao = expressoes_regulares['identificadores']
    caracteres_identificadores = []
    encontrar_palavras_com_numeros(programa)

    for token in programa:
        encontrar_caractere_nao_permitido(token)  # Verifica caracteres não permitidos dentro de cada token
        if re.match(padrao, token):
            caracteres_identificadores.append(token)

    return imprimir_identificadores(caracteres_identificadores)


def imprimir_identificadores(identificadores_encontrados):
    if not identificadores_encontrados:
        # print("Não há identificadores.")
        return False
    for identificadores in identificadores_encontrados:
        print(f"'{identificadores}' é um identificador.")
        return True


def encontrar_caractere_nao_permitido(programa):

    for token in programa:
        if token not in ignoraveis and not any(re.findall(padrao, token) for padrao in expressoes_regulares.values()):
            print(f"Erro: o token '{token}' contém caracteres não permitidos!")
            sys.exit()


def encontrar_palavras_com_numeros(programa):
    padrao = r'\b(\d+[a-zA-Z0-9_]*)\b'
    palavras_com_numeros = re.findall(padrao, programa)
    for palavra in palavras_com_numeros:
        if re.match('^\d', palavra):
            print(f'Erro: "{palavra}" é uma palavra inválida pois começa com um número.')
            sys.exit()

    # return programa


'''
def tokenize(programa):
    tokens = []
    token_atual = ""
    dentro_das_aspas = False

    for char in programa:
        if char == '"':
            if dentro_das_aspas:
                token_atual += char
                tokens.append(token_atual)
                token_atual = ""
                dentro_das_aspas = False
            else:
                if token_atual:
                    tokens.append(token_atual)
                    token_atual = ""
                dentro_das_aspas = True
                token_atual += char
        elif char.isspace():
            if token_atual and not dentro_das_aspas:
                tokens.append(token_atual)
                token_atual = ""
        else:
            token_atual += char

    if token_atual:
        tokens.append(token_atual)

    return tokens


def analisador_lexico(programa):
    programa = adicionar_espacos_delimitadores(programa)
    programa = adicionar_espacos_operadores(programa)
    print(programa)

    tokens = programa.split()  # Divide a string em tokens individuais

    for token in tokens:
        print(token)
        if encontrar_constantes_textuais(token):
            continue
        if encontrar_palavras_reservadas(token):
            continue
        if encontrar_operadores(token):
            continue
        if encontrar_numeros(token):
            continue
        if encontrar_delimitadores(token):
            continue
        if encontrar_identificadores(token):
            continue
        else:
            print(f"erro lexico {token}")
            sys.exit()


def adicionar_espacos_delimitadores(programa):
    delimitadores = r"[\(\)\[\]\{\};,:]"
    padrao = re.compile(f"({delimitadores})")

    string_formatada = padrao.sub(r' \1 ', programa)
    return string_formatada
    
    
def tokenize(programa):
    tokens = []
    token_atual = ""

    for char in programa:
        if char.isspace():
            if token_atual:
                tokens.append(token_atual)
                token_atual = ""
        else:
            token_atual += char

    if token_atual:
        tokens.append(token_atual)

    return tokens
    
    
def encontrar_numeros(programa):
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)
    imprimir_numeros(numeros_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def encontrar_constantes_textuais(programa):
    padrao = expressoes_regulares['constantes_textuais']
    constantes_encontradas = re.findall(padrao, programa)
    # nova_string = re.sub(padrao, lambda match: ' ', programa)
    return imprimir_constantes_textuais(constantes_encontradas)

def encontrar_caracteres_especiais(programa):
    padrao = expressoes_regulares['caracteres_especiais']
    caracteres_encontrados = re.findall(padrao, programa)
    imprimir_caracteres_especiais(caracteres_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string

    def encontrar_identificadores(programa):
    padrao = expressoes_regulares['identificadores']
    caracteres_identificadores = re.findall(padrao, programa)
    imprimir_identificadores(caracteres_identificadores)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def encontrar_identificadores(programa):
    encontrar_caractere_nao_permitido(programa)
    encontrar_palavras_com_numeros(programa)
    padrao = expressoes_regulares['identificadores']
    caracteres_identificadores = re.findall(padrao, programa)
    # nova_string = re.sub(padrao, lambda match: ' ', programa)
    return imprimir_identificadores(caracteres_identificadores)
    
def encontrar_caractere_nao_permitido(programa):
    for caractere in programa:
        if caractere not in caractere not in ignoraveis and not any(
                re.findall(padrao, caractere) for padrao in expressoes_regulares.values()):
            print(f"Erro: o caractere '{caractere}' não é permitido!")
            sys.exit()


def ler_arquivo(teste):
    f = open(teste, 'r')
    program = ""
    buffer = ""
    state = "DEFAULT"
    in_multiline_comment = False
    for line in f:
        i = 0
        while i < len(line):
            if state == "DEFAULT":
                if in_multiline_comment:
                    # Estamos dentro de um comentário de bloco, ignoramos tudo até encontrar o final do comentário
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                else:
                    # Verifica se há um comentário de linha
                    if line[i:i + 2] == "//":
                        break  # ignoramos o restante da linha
                    elif line[i:i + 2] == "/*":
                        # Início do comentário de bloco
                        in_multiline_comment = True
                        i += 1
                    else:
                        program += line[i]  # Adicionamos o caractere à string do programa
            else:
                # Estamos em um comentário de linha, ignoramos tudo até o final da linha
                break
            i += 1

        # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
        if state == "DEFAULT":
            if not in_multiline_comment:
                program += buffer
                buffer = ""

    f.close()
    return program



def ler_arquivo(teste):
    f = open(teste, 'r')
    program = ""
    buffer = ""
    state = "DEFAULT"
    in_multiline_comment = False
    in_quotes = False
    for line in f:
        i = 0
        while i < len(line):
            if state == "DEFAULT":
                if in_multiline_comment:
                    # Estamos dentro de um comentário de bloco, ignoramos tudo até encontrar o final do comentário
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                elif in_quotes:
                    if line[i:i + 1] in ["\"", "\'"]:
                        in_quotes = False
                    else:
                        pass
                else:
                    # Verifica se há um comentário de linha
                    if line[i:i + 2] == "//":
                        break  # ignoramos o restante da linha
                    elif line[i:i + 2] == "/*":
                        # Início do comentário de bloco
                        in_multiline_comment = True
                        i += 1
                    elif line[i:i + 1] in ["\"", "\'"]:
                        in_quotes = True
                        program += line[i]
                    else:
                        program += line[i]  # Adicionamos o caractere à string do programa
            else:
                # Estamos em um comentário de linha, ignoramos tudo até o final da linha
                break
            i += 1

        # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
        if state == "DEFAULT":
            if not in_multiline_comment and not in_quotes:
                program += buffer
                buffer = ""

    f.close()
    return program


def ler_arquivo(teste):
    f = open(teste, 'r')
    program = ""
    buffer = ""
    state = "DEFAULT"
    for line in f:
        i = 0
        while i < len(line):
            if state == "DEFAULT":
                if line[i:i + 2] == "//":
                    # Começamos um comentário de linha
                    break
                elif line[i:i + 2] == "/*":
                    # Começamos um comentário de bloco
                    state = "COMMENT_BLOCK"
                    i += 1
                else:
                    # Adicionamos o caractere à string do programa
                    program += line[i]
            elif state == "COMMENT_LINE":
                # Estamos em um comentário de linha, ignoramos tudo até o final da linha
                break
            elif state == "COMMENT_BLOCK":
                if line[i:i + 2] == "*/":
                    # Fim do comentário de bloco
                    state = "DEFAULT"
                    i += 1
                else:
                    # Adicionamos o caractere ao buffer
                    buffer += line[i]
            i += 1

        # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
        if state == "DEFAULT":
            program += buffer
            buffer = ""

    f.close()
    return program


def encontrar_numeros(programa):
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)

    for numero in numeros_encontrados:
        if re.match('^[a-zA-Z_]|(\d+[a-zA-Z]+)|([a-zA-Z]+\d+\w*)', numero):
            print(f'Erro: número não permitido encontrado: {numero}')
            exit()

    imprimir_numeros(numeros_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_numeros(numeros_encontrados):
    for num in numeros_encontrados:
        print(f"'{num}' é um Numeral.")



def encontrar_Palavras_Chave(programa):
    padrao = r"\b(" + "|".join(palavras_chave) + r")\b"
    palavras_chave_encontradas = re.findall(padrao, programa)
    return palavrasChave(palavras_chave_encontradas)

def encontrar_operadores(programa, operadores):
    padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    operadores_encontrados = re.findall(padrao, programa)
    return imprimir_operadores(operadores_encontrados)

def encontrar_caracteres_especiais(programa):
    padrao = expressoes_regulares['caracteres_especiais']
    caracteres_encontrados = re.findall(padrao, programa)
    return imprimir_caracteres_especiais(caracteres_encontrados)

def encontra_constantes_textuais(programa):
    in_quotes = False
    nova_string = ""
    frase = ''
    for i in range(len(programa)):
        if programa[i] == '"' or programa[i] == "'":
            in_quotes = not in_quotes
            if not in_quotes:
                print(f"'{frase}' é uma Constante Textual.")
                frase = ''
        elif in_quotes:
            frase += programa[i]
        else:
            nova_string += programa[i]
    return nova_string

'''
