print('What\'s the price with discount')

price = float(input('Price: '))
discount = float(input('Discount: '))

amount_to_discount = price * (discount / 100)
total = price - amount_to_discount

print('Total: {} - {}% = {}'.format(price, discount, total))