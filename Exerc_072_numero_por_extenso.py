while True:
        n = int(input('Digite um número entre zero e vinte: '))
        if n >= 20:
            numero_tupla = ('zero', 'um', 'dois', 'tres', 'quatro',
                            'cinco', 'seis', 'sete', 'oito', 'nove',
                            'dez', 'onze', 'doze', 'treze', 'catorze',
                            'quinze', 'dezesseis', 'dezessete', 'dezoito',
                            'dezenove', 'vinte')
            n = int(input('Digite um número entre zero e vinte: '))
            print(f'Você digitou o número {numero_tupla[n]}')
            break