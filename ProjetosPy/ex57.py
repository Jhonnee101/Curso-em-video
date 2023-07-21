sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos digite o seu sexo[M/F]')).strip().upper()[0]
print('Sexo {} registrad com sucesso'.format(sexo))