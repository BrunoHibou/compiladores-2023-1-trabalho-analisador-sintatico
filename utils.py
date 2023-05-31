from lexico import *
from sintatico import *
import re


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
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                else:
                    if line[i:i + 2] == "//":
                        break
                    elif line[i:i + 2] == "/*":
                        in_multiline_comment = True
                        i += 1
                    else:
                        program += line[i]
            else:
                break
            i += 1

        if state == "DEFAULT":
            if not in_multiline_comment:
                program += buffer
                buffer = ""

    f.close()
    return program


def iniciar_analisador(programa):
    programa = adicionar_espacos_delimitadores(programa)
    programa = adicionar_espacos_operadores(programa)
    print(programa)
    print("\n----------------------------------------------------\n")
    tokens = tokenize(programa)
    print(tokens)
    parse(tokens)


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
        elif dentro_das_aspas:
            token_atual += char
        elif char.isspace():
            if token_atual:
                tokens.append(token_atual)
                token_atual = ""
        else:
            token_atual += char

    if token_atual:
        tokens.append(token_atual)

    return tokens


def adicionar_espacos_delimitadores(programa):
    padrao_aspas = r'"(.*?)"'
    ocorrencias = re.findall(padrao_aspas, programa)
    marcador_espaco = "<ESPACO>"
    espacos_reservados = []

    for ocorrencia in ocorrencias:
        delimitador = f'"{ocorrencia}"'
        espacos = " " * len(ocorrencia)
        programa = programa.replace(delimitador, delimitador.replace(ocorrencia, marcador_espaco))
        espacos_reservados.append(ocorrencia)

    programa = re.sub(r'[\(\)\[\]\{\};,:]', r' \g<0> ', programa)

    for espaco_reservado in espacos_reservados:
        programa = programa.replace(marcador_espaco, espaco_reservado, 1)

    return programa


def adicionar_espacos_operadores(programa):

    resultado = ''
    entre_aspas = False

    for char in programa:
        if char == '"':
            entre_aspas = not entre_aspas

        if entre_aspas:
            resultado += char
        else:
            if char in operadores:
                resultado += ' ' + char + ' '
            else:
                resultado += char

    return resultado

