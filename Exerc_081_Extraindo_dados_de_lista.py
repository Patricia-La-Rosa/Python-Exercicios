lista =[]
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    #append para que os valores entrem na lista
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if 'N' in continuar:
        print('=-' * 30)
        print(f'Você digitou {len(lista)} elementos.')
        #len é usado para contar os elementos de dentro da lista
        lista.sort()
        #sort para colocar em ordem
        lista.reverse()
        #para reverter a ordem
        print(f'Os valores em ordem decrescente são {lista}')
        if 5 in lista:
            print('O valor 5 está na lista!')
        else:
            print('O valor 5 não está na lista!')
        break
