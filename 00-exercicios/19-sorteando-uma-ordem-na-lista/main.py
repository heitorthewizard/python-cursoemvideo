from random import shuffle

students = []

while True:
    student = input('Student\'s name or "done" if done: ')
    if student == 'done':
        break
    students.append(student)

shuffle(students)

students_length = len(students)
n = 0

print('The shuffled order is: ')
for student in students:
    print(student)
