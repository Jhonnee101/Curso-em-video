valores = []

valores.append(3)
valores.append(4)
valores.append(6)
valores.append(7)  

for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))
    valores.sort()

for c, v in enumerate(valores):
    print(f"Na posicao {c} encontrei o valor {v}")

for valor in valores:
    print(f"{valor}...",end="")

print("Cheguei ao final")