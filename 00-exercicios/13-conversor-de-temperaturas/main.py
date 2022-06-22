print('Temperature converter')
print('Choose your option down below:')
print('(1) Celcius to Fahrenheit')
print('(2) Kelvin to Fahrenheit')
print('(3) Fahrenheit to Celcius')
print('(4) Celsius to Kelvin')
print('(5) Kelvin to Celcius')
print('(6) Fahrenheit to Kelvin')
choice = int(input('Number: '))

if choice == 1:
    c = int(input('Value in Celcius: '))
    f = int(((9/5) * c) + 32)
    print('{}C = {}F'.format(c, f))

if choice == 2:
    k = int(input('Value in Kelvin: '))
    f = int(((9/5) * (k - 273)) + 32)
    print('{}K = {}F'.format(k, f))

if choice == 3:
    f = int(input('Value in Fahrenheit: '))
    c = int((5/9) * (f - 32))
    print('{}F = {}C'.format(f, c))

if choice == 4:
    c = int(input('Value in Celcius: '))
    k = int(c + 273)
    print('{}C = {}K'.format(c, k))

if choice == 5:
    k = int(input('Value in Kelvin: '))
    c = int(k - 273)
    print('{}K = {}C'.format(k, c))

if choice == 6:
    f = int(input('Value in Fahrenheit: '))
    k = int(((5/9) * (f - 32)) + 273)
    print('{}F = {}K'.format(f, k))

