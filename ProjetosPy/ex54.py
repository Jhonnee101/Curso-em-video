from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year
for pess in range(1, 8):
    nasc = int(input('Digite em que ano a {} pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1

print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))