from random import randint
print('Find out which number is gonna be printed between 0-5')

while True:
    num = int(input('Your Number: '))
    random_number = randint(0, 5)

    print('Number:', random_number)

    if num == random_number:
        print('Well Done, you made it!')
        break
    else:
        print('Sorry, try again')

