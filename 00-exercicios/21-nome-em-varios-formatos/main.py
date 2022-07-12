name = input('Enter your full name: ').strip()
upper_name = name.upper()
lower_name = name.lower()
full_name_length = len(name) - name.count(' ')
first_name_length = len(name.split()[0])

print(f'''
Uppercase = {upper_name}
Lowercase = {lower_name}
Full Name Length = {full_name_length}
First Name Length = {first_name_length} 
''')