n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O número {} é maior.'.format(n1))
elif n2 > n1:
    print('O número {} é maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais.')