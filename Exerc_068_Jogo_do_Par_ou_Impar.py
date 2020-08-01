from time import sleep
from random import randint
soma = 0
cont = 0
print('=-'*15)
print('VAMOS JOGAR PARA OU ÍMPAR')
print('=-'*15)
while True:
    v = int(input('Diga um valor: '))
    tipo = str(input('Par ou Ímpar? [P/I]')).strip()[0].upper()
    comp = randint (0,11)
    soma = comp + v
    if soma % 2 == 0:
        print('-' * 60)
        print(f'Você jogou {v} e o computador jogou {comp}. O total de {soma} - DEU PAR')
        print('-' * 60)
        if tipo == 'P':
            cont = cont + 1
            print('Você VENCEU! \n Vamos jogar novamente ...')
        else:
            print('Você PERDEU!')
            print('=-' * 15)
            print(f'GAME OVER. Você venceu {cont}')
            break
    else:
        print('-' * 60)
        print(f'Voce jogou {v} e o computador jogou {comp}. O total de {soma} - DEU ÍMPAR')
        print('-' * 60)
        if tipo == 'I':
            cont = cont + 1
            print('Você VENCEU! \n Vamos jogar novamente ...')
        else:
            print('Você PERDEU!')
            print('=-' * 15)
            print(f'GAME OVER. Você venceu {cont}')
            break