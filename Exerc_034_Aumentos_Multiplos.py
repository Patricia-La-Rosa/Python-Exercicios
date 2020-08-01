salario = float(input('Qual o salário do funcionário? R$ '))
if salario >= 1250:
    aument = (salario * 10 / 100)+ salario
    print('O seu salário é de R$ {:.2f} e com aumento de 10% será de R$ {:.2f}'.format(salario,aument))
else:
    print('O seu salário é de R$ {:.2f} e com o aumento de 15% será de R$ {:.2f}'.format(salario, ((salario*15)/100)+salario))
