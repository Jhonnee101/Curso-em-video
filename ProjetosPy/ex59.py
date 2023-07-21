primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
soma = 0
multiplicacao = 0
maior = primeiro
opcao = 0
while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NUMEROS NOVOS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Digite a sua opcao '))
    if opcao == 1:
        soma = primeiro + segundo
        print('O resultado de {} + {} = {}'.format(primeiro,segundo,soma))
    elif opcao == 2:
        multiplicacao = primeiro * segundo
        print('O resultado de {} X {} = {}'.format(primeiro,segundo,multiplicacao))
    elif opcao == 3:
        if primeiro < segundo:
            maior = segundo
            print('O maior entre os numeros é {}'.format(maior))
    elif opcao == 4:
        print('informe os numeros novamente:')
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida')

print('Fim do programa, volte sempre!')