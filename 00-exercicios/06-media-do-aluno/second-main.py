print('Student avarge grade')
grades = []

loop = True
answer = 'y'
total = 0
result = 0

while answer == 'y':
    grades.append(int(input('add grade: ')))
    answer = input('wish to add another grade?(y/n): ')

if answer == 'n': 
    try:
        for i in grades:
            total = total + i
            result = total / (len(grades))
        print('The students averge is {:.2f}'.format(result))
    except:
        print('you gave a wrong input, you must only add numerics')

