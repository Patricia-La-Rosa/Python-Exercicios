from time import sleep
def ajuda(com):
    while True:
        print('~ ' * 30)
        print('\033[0;30;42mSISTEMA DE AJUDA PyHELP\033[m')
        print('~ ' * 30)
        a = str(input(com)).lower()
        if a != 'fim':
            print('~ ' * 30)
            print(f'\033[1;30;46mAcessando o Manual do Comando {a} \033[m')
            print('~ ' * 30)
            sleep(1)
            print(help(a))
            sleep(1)
        else:
            break


#programa principal
a = ajuda('Função ou Biblioteca > ')