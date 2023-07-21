n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero[999 Para parar]: '))
    cont += 1
    soma += n
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont - 1, soma -999))
print('Fim')
