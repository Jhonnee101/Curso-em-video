listagem = ("1","Cerveja", 7.00,
            "2","Cachaca", 6.00,
            "3","Vodka", 9.00,
            "4","Espeto", 5.00,
            "5","Carne assada", 25.00,
            "6","Caldinho", 6.00,
            "7","Macaxeira", 3.00,
            "8","Batatinha", 10.00)
print("-" *30)
print("LISTAGEM DE PRECOS")
print("-" *30)
for pos in range(0,len(listagem)):
    if pos %3 == 0:
        print(f'{listagem[pos]:.<30}',end="")
    else:
        print(f"R${listagem[pos]:>5}")