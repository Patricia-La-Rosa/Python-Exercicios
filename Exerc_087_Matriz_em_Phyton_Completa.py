somapar = maior = somacoluna = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
#cria-se 3 listas
for l in range (0,3):
    # l de linha
    for c in range (0,3):
        # c de coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
#         esta primeira parte preenche minha matriz
print('=-'*30)
for l in range (0,3):
    # l de linha
    for c in range (0,3):
        # c de coluna
        print(f'[{matriz[l][c]:^5}]',end='')
        # esta segunda parte exibe a minha matriz como quero
        if matriz [l][c] % 2 ==0:
            somapar = somapar + matriz [l][c]
    print()
for l in range(0,3):
    somacoluna = somacoluna + matriz[l][2]
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c]>maior:
        maior = matriz[1][c]
print('=-'*30)
print(f'A soma de todos os valores pares digitados foi {somapar}')
print(f'A soma de todos os valores da terceira coluna foi {somacoluna}')
print(f'O maior valor da segunda linha foi {maior}')