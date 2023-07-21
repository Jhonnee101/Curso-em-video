v = float(input('Qual a velocidade do carro: '))
if v >80:
    m = (v-80) * 7
    print('Sua velocidade de {} esta acima do limite, você será multado em R${}'.format(v, m))
else:
    print('Sua velocidade esta abaixo do limite, continue assim')