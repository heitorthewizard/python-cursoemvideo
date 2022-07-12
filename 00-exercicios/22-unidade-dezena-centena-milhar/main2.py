# Mathematical way
number = int(input('Enter a number between 0-9999: '))

print(type(number))

if number >= 0 and number <= 9999:
    unit = number // 1 % 10
    decimal = number // 10 % 10
    hundred = number // 100 % 10
    thousand = number // 1000 % 10

    print('''
    Thousand: {}
    Hundred: {}
    Decimal: {}
    Unit: {}
    '''.format(thousand, hundred, decimal, unit))
