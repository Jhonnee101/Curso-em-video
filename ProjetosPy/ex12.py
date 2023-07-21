preço = float(input('Digite o valor de um produto'))
d = preço -(preço * 5/100)
print('O valor de {} com 5% de desconto fica de {:.2f}R$'.format(preço, d))