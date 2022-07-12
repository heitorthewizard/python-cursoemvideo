name = input('Enter your full name: ').strip().lower()

splitted_name = name.split()

print(f'''
First Name: {splitted_name[0].capitalize()}
Last Name: {splitted_name[-1].capitalize()}
''')
