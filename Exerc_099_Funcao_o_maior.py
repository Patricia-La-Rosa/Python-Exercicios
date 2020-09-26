def maior (* num):
    # se usa asterisco para indicar parametros desconhecidos
    cont = maior = 0
    print('=-'*30)
    print('Analisando os valores passados...')
    for valores in num:
        print(f'{valores}', end=' ')
        cont = cont + 1
        maior = max(num)
    print(f'foram informados {cont}')
    print(f'O maior valor informado foi {maior}')


# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
