from math import hypot
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
print('Sendo o valor do cateto oposto {} e do cateto adjacente {}, o valor da hipotenusa será {:.2f}.'.format(oposto, adjacente, hypot(oposto,adjacente)))
