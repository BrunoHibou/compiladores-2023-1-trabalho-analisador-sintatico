from utils import *


def main():
    nome = './testes/testeall.ptc'
    programa = ler_arquivo(nome)
    original = open(nome, 'r')
    print(original.read())
    print("\n----------------------------------------------------\n")
    iniciar_analisador(programa)

if __name__ == "__main__":
    print("----------------- Análise Iniciada -----------------\n")
    main()
