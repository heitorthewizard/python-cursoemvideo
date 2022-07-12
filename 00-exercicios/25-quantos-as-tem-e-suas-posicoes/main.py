text = input('Enter a text: ').strip().upper()
letters_array = list()

for letter in text:
    letters_array.append(letter)

letter_a_count = letters_array.count('A')
letter_a_positions = list()
count = 0

for letter in letters_array:
    if 'A' in letter:
        letter_a_positions.append(count)
    count += 1

first_and_last_position = [letter_a_positions[0], letter_a_positions[-1]]

print(f'''
How many 'A' is in the text: {letter_a_count}
Where are they: {letter_a_positions}
    first and last position: {first_and_last_position}
''')
