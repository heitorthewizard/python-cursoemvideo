from simple_colors import *

while True:
    unit = 0
    decimal = 0
    hundred = 0
    thousand = 0

    def print_numbers():
        print(f'''
        Thousand = {yellow(thousand)}
        Hundred = {yellow(hundred)}
        Decimal = {yellow(decimal)}
        Unit = {yellow(unit)}
        ''')

    print('enter "done" to stop')
    
    try:
        number = input('enter a number between 0-9999: ')   

        if number == 'done': break

        # it will check if the input is not a true number
        number = int(number)        
        number = str(number)


        if len(number) == 1 and int(number) >= 0:
            unit = number
            print_numbers()

        elif len(number) == 2 and int(number) >= 0:
            decimal = number[0]
            unit = number[1]
            print_numbers()

        elif len(number) == 3 and int(number) >= 0:
            hundred = number[0]
            decimal = number[1]
            unit = number[2]
            print_numbers()

        elif len(number) == 4 and int(number) >= 0:
            thousand = number[0]
            hundred = number[1]
            decimal = number[2]
            unit = number[3]
            print_numbers()

        else:
            print(red('[ERROR]: WRONG INPUT (Not between 0-9999)'))
    except:
        print(red('[ERROR]: WRONG INPUT (You must add a number)'))
