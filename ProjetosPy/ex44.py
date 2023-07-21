preco = float(input('Qual o valor das compras: RS'))
print('''FORMAS DE PAGAMENTO
[1] À vista
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
condi = int(input('Qual  sua opcao: '))
if condi == 1:
    desct = preco - (preco * 0.10)
    print('O valor das suas comprar com o desconto de 10% fica de R${}'.format(desct))
elif condi == 2:
    desct1 = preco - (preco * 0.05)
    print('O valor das suas comprar com o desconto de 5% fica de R${}'.format(desct1))
elif condi == 3:
    preco
    print('O valor das suas comprar fica de R${}'.format(preco))
else:
    juros = preco + (preco * 0.20)
    print('O valor das suas comprar parceladas com o juros fica de 20% fica de R${}'.format(juros))