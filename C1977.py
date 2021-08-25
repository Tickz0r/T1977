a = int (input ('Primeiro valor: '))
b = int (input ('Segundo valor: '))
c = int (input ('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('o maior número é {}'.format(b))
else:
    print('o maior numero é {}'.format(c))
print('Final da calculadora')