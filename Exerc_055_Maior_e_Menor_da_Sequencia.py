maior = 0
menor = 0
for p in range (1,6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
        #como esta é minha primeira variável ela é maior e menor no momento
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
