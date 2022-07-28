from simple_colors import *

print('Leap year checker')
year = int(input('Give me a year: '))

if (year % 4 == 0 and year % 100 != 0):
    print(green("It's a leap year"))
else:
    print(red("It's not a leap year"))

