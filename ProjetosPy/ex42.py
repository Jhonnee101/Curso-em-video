print('-=-'*10)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*10)

n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos abaixo formam um tringulo!')
    if n1 == n2 == n3:
        print('EQUILATERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos nao formam um triangulo')
