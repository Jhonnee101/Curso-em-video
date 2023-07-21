salario = float(input('Digite o seu salario: '))
if salario <= 1250:
    a = (salario * 0.10) + salario
    print('O seu salario com o aumento de 10% ficara R${:.2f}'.format(a))
else:
    a1 = (salario * 0.15) + salario
    print('O seu salario co o aumento de 15% ficara R${:.2f}'.format(a1))
