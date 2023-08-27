num = (2, 5, 9, 1)
num2 = [2, 5, 9, 1]
#num[2] = 3
num2[2] = 3
num2.append(7)
num2.insert(2,0)
num2.sort()
num2.pop() #Usa o pop para deletar o ultimo numero
#num2.sort(reverse=True) caso queira inverter a ordem
num2.remove(2) #Utiliza a funcao para deletar determinando o indice
if 4 in num2:
    num.remove(5)
else:
    print("Nao achei o numero 4")
print(num)
print(num2)
print(f"Essa lista tem {len(num2)} elementos.")