valor = float(input('Qual o valor da casa que voce dejesa comprar? '))
anos = int(input('Em quantos anos voce vai financiar? '))
salario = float(input('Qual o seu salario? '))
valorparcela = valor / (anos * 12)
salarioredu = salario * 0.30
if valorparcela >= salarioredu:
    print('O seu financiamento foi negado')
else:
    print('o seu financiamento foi aprovado')