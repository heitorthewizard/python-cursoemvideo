text = str(input('Enter a text: ')).strip().lower()

print('''
How many times A is shown? {}
Where is the first position? {}
WHere is the last position? {}
'''.format(text.count('a'), text.find('a'), text.rfind('a')))
