from datetime import date

ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('A sua categoria é: MIRIM')
elif idade <= 14:
    print('A sua categoria é: INFANTIL')
elif idade <= 19:
    print('A sua categoria é: JUNIOR')
elif idade <= 22:
    print('A sua categoria é: ADULTO')
else:
    print('A sua categoria é: SENIOR')