n1 = float(input('Digite o primero valor'))
n2 = float(input('Digite o segundo valor:'))
n3 = float(input('Digite o terceiro valor'))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1 
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))