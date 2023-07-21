n = str(input('Digite o seu nome: ')).strip()
nome = n.split()
print('Prazer em conhecer {}'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome)-1]))
