preco = float(input('Qual o preço do produto? R$ '))
valor_desc =float(input('Qual a % do desconto? '))
desconto = (preco-((preco*valor_desc)/100))
print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(preco,valor_desc,desconto))
