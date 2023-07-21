valor = float(input('Diga quanto voce tem em sua carteira:'))
d = valor / 5.74
eu = valor / 6.75
print('Com {:.2f}R$, voce compraria em dolar o valor de {:.2f} US$'.format(valor, d))
print('Com {:.2f}R$, voce compraria em euros o valor de {:.2f} EU$'.format(valor, eu))
