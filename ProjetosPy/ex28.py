import random

computador = random.randint(0, 5)
print('-=-'*19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*19)
jogador = int(input('Em qual número eu pensei? '))
if computador == jogador:
    print('Parabens, você acertou!!!')
else:
    print('Não foi dessa vez tente novamente!!!')