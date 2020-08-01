dias = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KM foram rodados? '))
pago = (dias * 60)+ (km * 0.15)
print ('O total a pagar é de R$ {:.2f}.'.format(pago))
