from lexico import analisador_lexico
from utils import *


def main():
    nome = './testes/teste2.ptc'
    programa = ler_arquivo(nome)
    original = open(nome, 'r')
    print(original.read())

    iniciar_analisador(programa)


if __name__ == "__main__":
    print("----------------- Programa Iniciado -----------------")
    main()
    print("----------------- Programa Finalizado -----------------")
