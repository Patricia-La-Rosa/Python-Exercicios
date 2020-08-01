lista = []
cont = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    lista.append([cont,nome,[n1,n2], media])
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if 'S' in continuar:
        cont = cont + 1
    else:
        break
print('=-'*15)
print(f'{"N°":<7}{"NOME":<10}{"MÉDIA":>8}')
print('--'*15)
for i, a in enumerate(lista):
    print(f'{i:<7}{a[1]:<14}{a[3]}')
while True:
    print('--'*15)
    aluno =int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO ...')
        break
    if aluno <= len(lista)-1:
        print(f'Notas de {lista[aluno][1]} são {lista[aluno][2]}')
print('<<<VOLTE SEMPRE>>>')


