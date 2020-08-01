soma = 0
cont = 0

for c in range (1,7):
    num1 = int(input('Digite o {} valor: '.format(c)))
    if num1 % 2 ==0:
        soma = soma + num1
        cont = cont + 1
print('Voce informou {} números pares e a soma foi {}.'.format(cont,soma))






