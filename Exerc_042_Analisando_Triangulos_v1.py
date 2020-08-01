r1 = float(input('Digite o comprimento da reta a: '))
r2 = float(input('Digite o comprimento da reta b: '))
r3 = float(input('Digite o comprimento da reta c: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estas medidas formarão um triângulo', end=' ')
    # o end ao final serve para agrupar com o proximo texto
    # se acontecer a opção acima, poderá ocorrer as opções abaixo
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isóceles')
    elif r1 != r2 or r1 != r2 or r2!= r3:
        print('Escaleno')
else:
    print('Essas medidas não formam um triângulo')