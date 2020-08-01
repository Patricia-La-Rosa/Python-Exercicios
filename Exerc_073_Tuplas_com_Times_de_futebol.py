times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')
print(f'Os times do campeonato Brasileiro de 2019 foram {times}')
print(f'Os 5 primeiros colocados do Campeonato Brasileiro de 2019 foram {times[0:5]}')
print(f'Os últimos 4 colocados foram {times[-4:]}')
print(f'ordem alfabética dos times é {sorted(times)}')
#ordem alfabética - sorted - não altera a tupla
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição.')
#deve-se colocar o mais 1 pois a contagem parte do 0