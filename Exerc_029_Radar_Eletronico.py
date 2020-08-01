velocidade = int(input("Qual a velocidade do carro? "))
if velocidade > 80:
    print('Sua velocidade foi de {}km/h, você foi multado.'.format(velocidade))
    print('O valor de sua multa será de R$ {:.2f}'.format((velocidade-80)*7))
else:
    print('Sua velocidade foi de {}km/h, você é um bom motorista. Parabéns!!!'.format(velocidade))
