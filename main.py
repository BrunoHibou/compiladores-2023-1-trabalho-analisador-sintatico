from utils import *


def main():
    nome = './testes/teste1.ptc'
    programa = ler_arquivo(nome)
    original = open(nome, 'r')
    print(original.read())

    iniciar_analisador(programa)


if __name__ == "__main__":
    print("----------------- Análise Iniciada -----------------")
    main()
