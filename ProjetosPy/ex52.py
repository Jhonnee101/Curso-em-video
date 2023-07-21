n = int(input('Digite um numero: '))
for c in range( 1, n+1):
    if n % c == 0:
        print('\33[34m', end=' ')
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')