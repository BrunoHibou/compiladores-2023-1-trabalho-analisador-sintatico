from dicionarios import *
import re
import sys


def analisador_lexico(token):
    print(token)
    auxiliar = encontrar_constantes_textuais(token)
    if not auxiliar:
        auxiliar = encontrar_palavras_reservadas(token)
        if not auxiliar:
            auxiliar = encontrar_operadores(token)
            if not auxiliar:
                auxiliar = encontrar_numeros(token)
                if not auxiliar:
                    auxiliar = encontrar_delimitadores(token)
                    if not auxiliar:
                        auxiliar = encontrar_identificadores(token)
                        if not auxiliar:
                            print(f"erro lexico {token}")
                            sys.exit()
    return auxiliar


def encontrar_palavras_reservadas(programa):
    padrao = r"\b(" + "|".join(palavras_reservadas) + r")\b"
    palavras_reservadas_encontradas = re.findall(padrao, programa)
    return palavrasReservadas(palavras_reservadas_encontradas)


def palavrasReservadas(palavras_reservadas_encontradas):
    if not palavras_reservadas_encontradas:
        return False
    for palavra in palavras_reservadas_encontradas:
        print(f"'{palavra}' é uma Palavra Reservada.")
        return palavra


def encontrar_operadores(programa):
    padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    operadores_encontrados = re.findall(padrao, programa)
    return retornar_operadores(operadores_encontrados)


def retornar_operadores(operadores_encontrados):
    if not operadores_encontrados:
        return False
    for op in operadores_encontrados:
        print(f"'{op[1]}' é um Operador.")
        return op[1]


def encontrar_numeros(programa):
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)
    inteiros = [num for num in numeros_encontrados if '.' not in num]
    floats = [num for num in numeros_encontrados if '.' in num]

    resposta = retornar_numeros(inteiros, 'Inteiro')
    if resposta:
        return resposta
    else:
        resposta = retornar_numeros(floats, 'Flutuante')

    return resposta


def retornar_numeros(numeros, tipo):
    if not numeros:
        return False
    for num in numeros:
        print(f"'{num}' é um numeral {tipo}.")
        return "NUMBER"


def encontrar_constantes_textuais(programa):
    padrao = expressoes_regulares['constantes_textuais']
    constantes_encontradas = re.findall(padrao, programa)
    return retornar_constantes_textuais(constantes_encontradas)


def retornar_constantes_textuais(constantes_encontradas):
    if not constantes_encontradas:
        return False
    for constante in constantes_encontradas:
        print(f"'{constante}' é uma Constante Textual.")
        return "STRING"


def encontrar_delimitadores(programa):
    padrao = expressoes_regulares['delimitadores']
    delimitadores_encontrados = re.findall(padrao, programa)
    return retornar_delimitadores(delimitadores_encontrados)


def retornar_delimitadores(delimitadores_encontrados):
    if not delimitadores_encontrados:
        return False
    for caracteres in delimitadores_encontrados:
        print(f"'{caracteres}' é um Delimitador.")
        return caracteres


def encontrar_identificadores(programa):
    padrao = expressoes_regulares['identificadores']
    caracteres_identificadores = []
    encontrar_palavras_com_numeros(programa)

    for token in programa:
        encontrar_caractere_nao_permitido(token)  # Verifica caracteres não permitidos dentro de cada token
        if re.match(padrao, token):
            caracteres_identificadores.append(token)

    return retornar_identificadores(caracteres_identificadores)


def retornar_identificadores(identificadores_encontrados):
    if not identificadores_encontrados:
        return False
    for identificadores in identificadores_encontrados:
        print(f"'{identificadores}' é um identificador.")
        return "IDENTIFIER"


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
