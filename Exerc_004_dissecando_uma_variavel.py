a = (input('Digite algo: '))
print('O tipo primitivo deste valor é {}'.format(type(a)))
print('Só tem espaço? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em maiúscula? {}'.format(a.isupper()))
print('Está em minúscula? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))