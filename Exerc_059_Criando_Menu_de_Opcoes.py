from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('OPÇÕES: \n [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
    op = int(input('>>>>> Qual a sua opção? '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1,n2,soma))
        print('=-'*20)
        sleep(3)
    elif op == 2:
        multi = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1,n2,multi))
        print('=-' * 20)
        sleep(3)
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n2))
            print('=-' * 20)
        sleep(3)
    elif op == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-' * 20)
print('Fim do programa. Volte sempre!')

