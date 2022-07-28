wage = float(input('Enter the wage: '))

if wage > 1250:
    increase = wage * 0.10
    total = wage + increase
    print(f'''
Above $1250, raise of 10%

Then: ${format(wage, ".2f")}
Now: ${format(total, ".2f")}
    ''')
else:
    increase = wage * 0.15
    total = wage + increase
    print(f'''
Below $1250, raise of 15%

Then: ${format(wage, ".2f")}
Now: ${format(total, ".2f")}
    ''')

