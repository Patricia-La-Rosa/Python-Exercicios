from time import sleep
conteudo: ()

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            print(linha())
        except (ValueError,TypeError):
            print('\033[0;31mERRO. Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO. O usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n


def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[0;33m{c} - \033[m \033[0;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[0;32mSua Opção: \033[m')
    return opc






