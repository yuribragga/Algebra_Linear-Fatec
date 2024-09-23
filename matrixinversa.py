import sympy as sp
import numpy as np

def matriz_inversa():
    colunas = 4
    linhas = 4
    matriz = []

    print('Digite os valores da matriz linha por linha')

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            try:
                valor = int(input(f'Digite o valor da posição {i+1}x{j+1}: '))
                linha.append(valor)
            except ValueError:
                print('Valor inválido! Digite um número inteiro.')
                return
        matriz.append(linha)

    print("\nMatriz original:")
    for linha in matriz:
        print(linha)

    np_matriz = np.array(matriz)

    determinante = np.linalg.det(np_matriz)

    if determinante == 0:
        print("\nA matriz não é inversível (determinante igual a zero).")
        return
    else:
        # Calculando a inversa
        matriz_inversa = np.linalg.inv(np_matriz)

        print("\nMatriz inversa:")
        print(matriz_inversa)

    print('Pressione Enter para usar uma variável simbólica')
    
    # Função auxiliar para verificar entrada
    def obter_valor(variavel, simbolo):
        valor = input(f'Digite o valor de {variavel}: ')
        if valor == '':
            return sp.symbols(simbolo)
        return int(valor)

    re = obter_valor('RE', 'x')
    p1 = obter_valor('P1', 'y')
    p2 = obter_valor('P2', 'w')
    rd = obter_valor('RD', 'z')
    modulo_elasticidade = obter_valor('E (módulo de elasticidade)', 'E')
    area = obter_valor('A (área)', 'A')
    comprimento = obter_valor('L (comprimento)', 'L')

    vetor_forca = [
        re * ((modulo_elasticidade * area) / comprimento),
        p1 * ((modulo_elasticidade * area) / comprimento),
        p2 * ((modulo_elasticidade * area) / comprimento),
        rd * ((modulo_elasticidade * area) / comprimento)
    ]

    solucao = []
    for i in range(len(matriz_inversa)):
        soma = 0
        for j in range(len(matriz_inversa)):
            soma += matriz_inversa[i][j] * vetor_forca[j]
        solucao.append(soma)

    # Forçando os deslocamentos U1 e U4 a serem 0
    solucao[0] = 0
    solucao[-1] = 0

    print("\nSolução final:")
    for resultado in solucao:
        print(resultado)

matriz_inversa()
