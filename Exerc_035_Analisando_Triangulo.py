r1 = float(input('Digite o valor da reta a: '))
r2 = float(input('Digite o valor da reta b: '))
r3 = float(input('Digite o valor da reta c: '))
print('-='*25)
print('Analisador de Triângulos')
print('-='*25)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas medidas podem formam um triangulo')
else:
    print('Essas medidas NÃO podem formam um triangulo')
