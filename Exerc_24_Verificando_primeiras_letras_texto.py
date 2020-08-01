cid = str(input('Digite a cidade que você nasceu: ')).strip()
# coloco o strip para retirar possíveis espaços antes e depois
print(cid[:5].upper() == 'SANTO')
# com o upper transformo tudo em maisculo tornando true