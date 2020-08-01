numeros = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
        #verificar um número que não está na lista
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar != 'N':
        print('Valor adicionado com sucesso ...')
    else:
        numeros.sort()
        #para colocar em ordem a lista
        print('=-' * 20)
        print(f'Você digitou os valores {numeros}')
        break