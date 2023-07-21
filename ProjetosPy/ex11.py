a = float(input('Qual a altura de sua parede:'))
l = float(input('Qual a largura de sua parede:'))
area = a * l
t = area / 4
print('Para pintar uma parede de {} metros quadrados será necessario {:.2f} Litros de tinta'.format(area, t))