print('Paycheck raise')

paycheck = float(input('What\'s your paycheck? '))
raise_porcentage = float(input('what\'s the raise porcentage? '))

the_raise = paycheck * (raise_porcentage / 100)
raise_itself = paycheck + the_raise

print('{} + {}% = {}'.format(paycheck, raise_porcentage, raise_itself))
