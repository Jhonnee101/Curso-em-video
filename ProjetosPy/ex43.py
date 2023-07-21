peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura * altura)

if imc <=18.5:
    print('Voce está muito magro, coma bastante')
elif imc <=25.0:
    print('Voce está em um peso ideal, parabens!!!')
elif imc <=30:
    print('Voce está com sobrepeso, cuide-se')
elif imc <= 40:
    print('Voce está obeso, vai ter um infarto')
else:
    print('Coma enquanto pode, porque logo logo não vai poder comer mais...')