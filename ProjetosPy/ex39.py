from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
alistamento = date.today().year - ano
if alistamento < 18:
    resta = 18 - alistamento
    print('Voce ainda esta muito novo para se alistar, ainda lhe falta {} anos'.format(resta))
elif alistamento == 18:
    print('Esta no momento de voce servir esse país')
else:
    atraso = 18 - alistamento
    print('Voce esta atrasado {} anos, vá se alistar imediatamente'.format(atraso))
