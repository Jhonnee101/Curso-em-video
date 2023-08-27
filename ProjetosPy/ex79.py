numeros = list()

while True:
    n = int(input("Digite um numero: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado")
        numeros.remove(n)
    r = str(input("Quer continuar[S/N]"))
    numeros.append(n)
    if r in "Nn":
        break

print(f"{numeros}")
