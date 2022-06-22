from random import choice
from time import sleep

students = []
number_of_students = 0
answer = 'n'

while True:
    number_of_students = number_of_students + 1
    student = input('Student\'s name: ')
    students.append(student)
    answer = input('add another student? (y/n): ')

    if answer == 'n':
        break

random_student = choice(students)

print('Getting a random student...')
sleep(2)
print(f'The chosen student is {random_student.upper()}')
