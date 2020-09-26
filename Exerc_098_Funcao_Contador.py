from time import sleep
lista = list()
def contador():
    print('-='*30)
    print(f'Contagem de 1 a 10 de 1 em 1')
    for x in range(1,11,1):
        print(f'{x}', end=' ')
    print('FIM!!')
    sleep(1)


def contadorrev ():
    print('-='*30)
    print(f'Contagem de 10 até 0 de 2 em 2')
    for x in range(10,-1,-2):
        # para reverter o range uso o -1 no stop
        print(f'{x}', end=' ')
    print('FIM!!')
    sleep(1)


def contadopers (i,f,p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for x in range(i,f,p):
        # para reverter o range uso o -1 no stop
        print(f'{x}', end=' ')
    print('FIM!!')
    print('-=' * 30)



# programa principal
contador()
contadorrev()
print('-='*30)
print('Agora é sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contadopers(i,f,p)
