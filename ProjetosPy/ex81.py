cont = 0
numeros = []
resposta = 'S'

while resposta in 'S':
        num = numeros.append(int(input("Digite um valor: ")))
        resposta = str(input('Dejesa continuar [S/N]')).upper().strip()[0]
        cont += 1

numeros.sort(reverse=True)
print(f"Voce digitou {cont} vezes.")
print(f"Os valores digitados em ordem decresente foram {numeros}")
if 5 in numeros:
    print(f"O valor 5 está na lista na posição",numeros.index(5))
else:
    print("O 5 não está na lista")