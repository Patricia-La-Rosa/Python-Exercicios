km = int(input('Qual a distância desta viagem em KM?: '))
perto = 0.5
longe = 0.45
if (km <= 200):
    print("O custo de sua viagem será de R$ {:.2f}".format(km*perto))
else:
    print('O custo de sua viagem será de R$ {:.2f}'.format(km*longe))
