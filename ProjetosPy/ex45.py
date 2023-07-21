from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Escolha uma opcao:
[0] Pedra
[1] Papel
[2] Tesoura''')
escolha = int(input('Sua escolha: '))
print('-='*11)
print('O jogador jogou {}'.format(itens[escolha]))
print('O computador jogou {}'.format(itens[computador]))
print('-='*11)
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('POH!')
sleep(1)
if computador == 0:
    if escolha == 0:
        print('EMPATOU')
    elif escolha == 1:
        print('JOGADOR VENCE')
    elif escolha == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida!!!')
elif computador == 1:
    if escolha == 0:
        print('COMPUTADOR VENCE')
    elif escolha == 1:
        print('EMPATOU')
    elif escolha == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida!!!')
elif computador == 2:
    if escolha == 0:
        print('JOGADOR VENCE')
    elif escolha == 1:
        print('COMPUTADOR VENCE')
    elif escolha == 2:
        print('EMPATOU')
    else:
        print('Jogada invalida!!!')