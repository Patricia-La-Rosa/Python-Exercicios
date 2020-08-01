from datetime import date
atual = date.today().year
count = 0
count1 = 0
for c in range (1,8):
    ano = int(input('Em que ano a {}a pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 18:
        count = count + 1
    else:
        count1 = count1 + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(count))
print('E também tivemos {} pessoas menores de idade'.format(count1))
