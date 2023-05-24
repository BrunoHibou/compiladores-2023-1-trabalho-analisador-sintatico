from lexico import analisador_lexico
from utils import *


def main():
    nome = './testes/teste1.c'
    programa = ler_arquivo(nome)
    original = open(nome, 'r')
    print(original.read())

    analisador_lexico(programa)

    '''print('-----------------\n' + programa + '\n-----------------\n')
    encontrar_constantes_textuais(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    encontrar_Palavras_Reservadas(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    encontrar_operadores(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    encontrar_numeros(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    encontrar_delimitadores(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    encontrar_identificadores(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')

'''
if __name__ == "__main__":
    print("----------------- Programa Iniciado -----------------")
    main()
    print("----------------- Programa Finalizado -----------------")
