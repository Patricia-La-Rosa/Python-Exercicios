n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando nota {} e {} sua média foi de {:.1f}.'.format(n1,n2,media))
if (media < 5):
    print ('Você foi REPROVADO')
elif (media >= 5) and (media < 7):
    print('Você está em RECUPERAÇÃO')
else:
    print('Você foi APROVADO')



