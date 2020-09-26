from Exerc_109_Exercitando_Modulos import moeda

preco = float(input('Digite o valor: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}')
print(f'O dobro do preço de {moeda.moeda(preco)} é {moeda.dobro(preco,True)}')
print(f'Com aumento de 10% fica em {moeda.aumentar(preco, 10, True)}.')
print(f'Com redução de 10% fica em {moeda.diminuir(preco, 10, True)}.')
