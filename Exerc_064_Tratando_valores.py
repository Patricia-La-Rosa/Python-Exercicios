n = int(input('Digite um número [999 para parar]: '))
count = 0
total = 0
while n != 999:
    count = count + 1
    total = total + n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi de {}'.format(count,total))