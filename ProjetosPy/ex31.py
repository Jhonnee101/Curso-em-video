d = int(input('Qual a distancia da sua viagem?'))
if d <= 200:
    c = d*0.50
    print('Para percorrer {} Km, o custo será de R${}'.format(d, c))
else:
    c1 = d*0.45
    print('Para percorrer {} Km, o custo será de R${}'.format(d, c1))