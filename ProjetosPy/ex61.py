print('Gerador de PA')
print('=-'*7)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')