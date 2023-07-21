soma = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite um numero qualquer: '))
    if n % 2 == 0:
        soma = soma + n
        count = count + 1
print('Voce informou {} numeros pares e a soma foi {}'.format(count, soma))