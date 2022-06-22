from math import sqrt, ceil

print('Raíz quadrada de um número')

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))

