n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2 
if media < 5.0:
    print('Sua media foi muito baixa, está reprovado')
elif media <= 6.9:
    print('Sua media foi baixa, está de recuperacao')
else:
    print('Parabens sua media foi boa, voce esta aprovado')