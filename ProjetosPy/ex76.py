listagem = ("Cerveja", 7.00,
             "Cachaca", 6.00,
             "Vodka", 9.00,
             "Espeto", 5.00,
             "Carne assada", 25.00,
             "Caldinho", 6.00,
             "Macaxeira", 3.00,
             "Batatinha", 10.00)
print("-" *30)
print("LISTAGEM DE PRECOS")
print("-" *30)
for pos in range(0,len(listagem)):
    if pos %2 == 0:
        print(f'{listagem[pos]:.<30}',end="")
    else:
        print(f"R${listagem[pos]:>5}")