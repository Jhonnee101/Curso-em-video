dias = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos Km foram rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}R$'.format(pago))