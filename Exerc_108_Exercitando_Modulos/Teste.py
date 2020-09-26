from Exerc_108_Exercitando_Modulos import moeda

preco = float(input('Digite o valor: '))
taxa = 10
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro do preço de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O preço de {moeda.moeda(preco)} com aumento de 10% fica em {moeda.moeda(moeda.aumentar(preco, taxa))}.')
print(f'O preço de {moeda.moeda(preco)} com diminuição de 10% fica em {moeda.moeda(moeda.diminuir(preco, taxa))}.')
