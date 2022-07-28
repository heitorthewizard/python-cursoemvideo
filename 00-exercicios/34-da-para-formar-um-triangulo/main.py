count = 1
lines = list()

while count < 4:
    line = float(input(f'Give me the line {count}: '))
    lines.append(line)
    count += 1

if (
    lines[0] + lines[1] > lines[2] and
    lines[0] + lines[2] > lines[1] and
    lines[1] + lines[2] > lines[0]
):
    print('It can build a triangle')
else:
    print('It cannot be a triangle')

