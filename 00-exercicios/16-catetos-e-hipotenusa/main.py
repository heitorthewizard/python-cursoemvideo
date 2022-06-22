import math

perpendicular = float(input('Perpendicular value: '))
base = float(input('Base valeu: '))

hypotenuse = math.hypot(perpendicular, base)

print(f'hypotenuse: {hypotenuse}')
