resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Dejesa continuar [S/N]')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
print(soma)
print('fim')