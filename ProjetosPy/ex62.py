print('Gerador de PA')
print('=-'*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print ('{} -> '.format (termo), end= '')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais voce quer mostrar? '))
print('Progressao finalizada, o total de termos foi de {}'. format(total))
print('FIM')
