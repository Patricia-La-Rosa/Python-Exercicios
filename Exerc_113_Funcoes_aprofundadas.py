def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO. Digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mERRO. O usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[0;31mERRO. Digite um número real válido.\033[m')
        else:
            return r


# programa principal
n = leiaInt('Digite um número inteiro? ')
r = leiafloat('Digite um número real? ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {r}.')
