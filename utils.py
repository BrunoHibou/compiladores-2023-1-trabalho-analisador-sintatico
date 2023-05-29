from dicionarios import *
from lexico import *
from sintatico import *
import re
import sys


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


def iniciar_analisador(programa):
    programa = adicionar_espacos_delimitadores(programa)
    programa = adicionar_espacos_operadores(programa)
    print(programa)

    tokens = tokenize(programa)  # Converte os tokens um por um
    '''n = 0
    for token in tokens:
        #print(token)
        n = analisador_lexico(token)
        print(n)
    '''
    print(tokens)
    parse(tokens)
'''    
    try:
        # Criação do analisador sintático
        parser = Parser(tokens)
        parser.parse()
        print("Análise sintática concluída com sucesso!")
    except SyntaxError as e:
        print(f"Erro de sintaxe: {str(e)}")
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
    operadores_auxiliar = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    padrao = re.compile(f"({operadores_auxiliar})")

    string_formatada = padrao.sub(lambda m: m.group(1) if m.group(1) else ' ' + m.group(2) + ' ' if m.group(2) else ' ',
                                  programa)
    return string_formatada


'''
def iniciar_analisador(programa):
    programa = adicionar_espacos_delimitadores(programa)
    programa = adicionar_espacos_operadores(programa)
    print(programa)

    tokens = tokenize(programa)  # Converte os tokens um por um
    print(tokens)
    # Lista de tokens obtidos através do analisador léxico
    analisador_lexico(tokens)
    # Criação do analisador sintático
    parser = Parser(tokens)
    print(tokens)
    try:
        # Inicia a análise sintática
        parser.parse()
        print("Análise sintática concluída com sucesso!")
    except SyntaxError as e:
        print(f"Erro de sintaxe: {str(e)}")



def adicionar_espacos_operadores(programa):
    operadores_auxiliar = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    padrao = re.compile(f"({operadores_auxiliar})")

    string_formatada = padrao.sub(r' \1 ', programa)
    return string_formatada'''
