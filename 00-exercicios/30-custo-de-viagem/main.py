print('Measuring travel cost')
distance = float(input('Tell me how far is your goal in Km: '))

if (distance <= 200):
    cost = distance * 0.50
    print('Your travel will cost ${:.2f}'.format(cost))
else:
    cost = distance * 0.45
    print('Your travel will cost ${:.2f}'.format(cost))

print('Have a good travel!')

