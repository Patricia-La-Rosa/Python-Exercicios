peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f} e seu status é ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de {:.1f} e seu status é PESO IDEAL'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é de {:.1f} e seu status é SOBREPESO'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é de {:.1f} e seu status é OBESIDADE'.format(imc))
else:
    print('Seu IMC é de {:.1f} e seu status é OBESIDADE MÓRBIDA'.format(imc))


