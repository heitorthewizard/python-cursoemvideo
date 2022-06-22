is_num = input('give any value: ')

if is_num.isnumeric():
    print('{} is numeric'.format(is_num))

if is_num.isalpha():
    print('{} is alphabetic'.format(is_num))

if is_num.isalnum():
    print('{} is alphanumeric'.format(is_num))

if is_num.isupper():
    print('{} is upper case'.format(is_num))

if is_num.islower():
    print('{} is lower case'.format(is_num))

print(type(is_num))
