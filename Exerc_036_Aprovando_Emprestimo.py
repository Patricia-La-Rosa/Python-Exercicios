valor = float(input('Qual o valor da casa que você pretende financiar: R$ '))
salario = float(input('Qual o seu salário: R$ '))
anos = int(input('Em quantos anos você pretende pagar: '))
presta = valor / (anos*12)
porc = (salario*30)/100
print('Para pagar um casa de R$ {:.2f} em {} anos, sua prestação será de R$ {:.2f}, portanto:'.format(valor,anos, presta))
if presta <= porc:
    print('Seu empréstimo no valor de R$ {:.2f} foi APROVADO'.format(valor))
else:
    print('Seu empréstimo de {:.2f} foi NEGADO'.format(valor))