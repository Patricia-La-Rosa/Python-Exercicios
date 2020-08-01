import random
# primeira maneira de resolver

# list = ['Paulo', 'Ana', 'Pedro', 'Maria']
# print('Primeiro aluno: {}'.format(list[0]))
# print('Segundo aluno: {}'.format(list[1]))
# print('Terceiro aluno: {}'.format(list[2]))
# print('Quarto aluno: {}'.format(list[3]))
# sorteio = random.choice(list)
# print('O aluno escolhido foi {}'.format(sorteio))

# segunda maneira de resolver

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Primeiro aluno: '))
n3 = str(input('Primeiro aluno: '))
n4 = str(input('Primeiro aluno: '))
list = [n1, n2, n3, n4]
sorteio = random.choice(list)
print('O aluno escolhido foi {}'.format(sorteio))