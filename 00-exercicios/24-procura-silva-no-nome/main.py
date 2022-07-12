from simple_colors import * 

name = str(input('Enter your full name: ')).strip().lower()

if name.find('silva') != -1:
    print(green('It has Silva in it'))
else:
    print(red('It doesn\'t have Silva in it'))
