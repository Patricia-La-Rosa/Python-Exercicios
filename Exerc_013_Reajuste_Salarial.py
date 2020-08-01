sal = float(input('Qual o salário do funcionário? '))
aumento_porc = float(input('De quanto será o aumento em %? '))
aumento_real = sal+((sal*aumento_porc)/100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}.'.format(sal,aumento_porc,aumento_real))

