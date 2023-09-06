lista = []
pares = []
impares = []
resp = 'S'
while resp in 'S':
    num = int(input("Digite um numero: "))
    lista.append(num)
    resp = str(input('Dejesa continuar [S/N]')).upper().strip()[0]
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"A lista com todos os valores foi",lista)
print(f"Os valores pares digitados foram",pares)
print(f"Os valores impares digitados foram",impares)