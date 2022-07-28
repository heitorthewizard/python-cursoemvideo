program = 'The biggest and the smallest of them'

print('=' * len(program))
print(program)
print('=' * len(program))

count = 1
num_arr = list()

while True:
    num = input(f'Give me a number or enter "done" to stop: ').strip()
    
    if num == 'done': break
    else: num = float(num)

    num_arr.append(num)
    count += 1

biggest = max(num_arr)
smallest = min(num_arr)

print(f''''
From all these numbers below:
{num_arr}

The biggest number is {biggest}
The smallest number is {smallest}
''')

