n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** 2

print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d))
print('A divisão inteira {} e potência {}'.format(di, e))

