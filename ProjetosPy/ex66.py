soma = cont = 0
while True:
    n = int(input('Digite um numero[Digite 999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} numeros deu {soma}')

    

