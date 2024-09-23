import sympy as sp

def matriz():
    colunas = 4
    linhas = 4
    matriz = []

    print('Digite os valores da matriz linha por linha')

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f'Digite o valor da posição {i+1}x{j+1}: '))
            if valor == '':
                print('Digite um valor válido')
                return matriz()
            else:
                linha.append(valor)
        matriz.append(linha)

    print(matriz)

    print('Pressione Enter para não digitar um valor e usar uma variável simbólica')

    u2 = input('Digite o valor de U2: ')
    if u2 == '':
        u2 = sp.symbols('U2') 
    else:
        u2 = int(u2)

    u3 = input('Digite o valor de U3: ')
    if u3 == '':
        u3 = sp.symbols('U3') 
    else:
        u3 = int(u3)

    modulo_elasticidade = input('Digite o valor de E (módulo de elasticidade): ')
    if modulo_elasticidade == '':  
        modulo_elasticidade = sp.symbols('E') 
    else:
        modulo_elasticidade = int(modulo_elasticidade)

    area = input('Digite o valor de A (área): ')
    if area == '':
        area = sp.symbols('A')
    else:
        area = int(area)

    comprimento = input('Digite o valor de L (comprimento): ')
    if comprimento == '':
        comprimento = sp.symbols('L')
    else:
        comprimento = int(comprimento)

    vetor_forca = [0, u2 * ((modulo_elasticidade * area) / comprimento), u3 * ((modulo_elasticidade * area) / comprimento), 0]

    solucao = []
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz)):
            soma += matriz[i][j] * vetor_forca[j]
        solucao.append([soma])

    print(solucao)
    print("O valor de RE é:", solucao[0][0], "O valor de RD é:", solucao[3][0])

matriz()
