num = int(input('Give me any integer number: '))

n = 1
result = 0

while n <= 10:
    result = num * n
    print('{} x {} = {} '.format(num, n, result))
    n = n + 1

