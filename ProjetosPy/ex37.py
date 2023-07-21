from binhex import hexbin


n = int(input('Digite um número inteiro: '))
print('''Digite o numero referente a base de conversao:
[1] Converter para Binario:
[2] converter para Hexadecimal
[3] Converter para Octal''')
opcao = int(input('Sua opcao: '))

if opcao == 1:
    print('{} Convertido para BINARIO ficaria {}'.format(n, bin(n)))
elif opcao == 2:
    print('{} Convertido para HEXADECIMAL ficaria {}'.format(n, hex(n)))
elif opcao == 3:
    print('{} Convertido para OCTAL ficaria {}'.format(n, oct(n)))
else:
    print('Opcao invalida')