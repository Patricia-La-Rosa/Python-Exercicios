menor = 0
maior = 0
valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
#desta maneira crio uma lista e append serve para adicionar e cont para indicar a posição
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('='*40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i} ...', end='')
print()
# este print é usado para quebrar a linha
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i} ...', end='')
