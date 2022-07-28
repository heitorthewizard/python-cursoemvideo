a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

smallest = a

if b < a and b < c:
    smallest = b

if c < a and c < b:
    smallest = c

biggest = a

if b > a and b > c:
    biggest = b

if c > a and c > b:
    biggest = c

print(f'O menor valor é {smallest}')
print(f'O maior valor é {biggest}')

