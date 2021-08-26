a = int (input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou o primeiro bimestre errado:'))
b = int (input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou o segundo bimestre errado:'))
c = int (input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou o terceiro bimestre errado:'))
d = int (input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou o quarto bimestre errado:'))

media = (a + b + c + d) / 4
print('media: {}'.format(media))
#if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#    print('média {}'. format(media))
#else:
#    print('Foi informado alguma nota errada')