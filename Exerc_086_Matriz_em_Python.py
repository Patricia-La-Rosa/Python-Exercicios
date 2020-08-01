matriz = [[0,0,0],[0,0,0],[0,0,0]]
#cria-se 3 listas
for l in range (0,3):
    # l de linha
    for c in range (0,3):
        # c de coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-'*30)
for l in range (0,3):
    # l de linha
    for c in range (0,3):
        # c de coluna
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

