print('Car Rent')
print('Day: R$60 || Km: R$0.15')
day = int(input('How many days: '))
km = float(input('How many kilometers: '))

total_payment = (day * 60) + (km * 0.15)

print('Total: {} for {} days and {}km'.format(total_payment, day, km))

