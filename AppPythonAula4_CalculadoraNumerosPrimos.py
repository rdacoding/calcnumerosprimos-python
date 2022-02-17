a = int(input('Valor a ser analisado: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1

if div == 2:
    print('Numero {} e primo'.format(a))
else:
    print('Numero {} nao e primo'.format(a))