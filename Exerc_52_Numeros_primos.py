num = int(input('Digite um número: '))
total = 0


for c in range (1,num+1):
    if num % c == 0:
        print('\033[031m', end=' ')
    #     codigo para cores
        total = total+1
        # vc pode usar total += 1 (significa o mesmo)
    else:
        print('\033[34m',end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi divisível {} vezes'.format(num,total))
if total == 2:
    print(' O número {} é PRIMO.'.format(num))
else:
    print(' O número {} não é PRIMO.'.format(num))


