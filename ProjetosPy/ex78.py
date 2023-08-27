lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor para a posicao {c}: ")))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            men = lista[c]
lista.sort()
print(f"Voce digitou os valores {lista}")
print(f"O maior valor digitado foi: {maior}, na posicao",end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...",end="")
print(f"O menor valor digitado foi: {menor}, na posicao",end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...",end="")