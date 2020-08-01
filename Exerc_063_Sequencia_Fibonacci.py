print('-' * 25)
print('Sequência de Fibonacci')
print('-'* 25)
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = t1 + t2
count = 3
print('~'*30)
print('{}---{}---'.format(t1,t2),end='')
while count <= termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{}---'.format(t3),end='')
    count = count + 1
print('FIM')
print('~'*30)

