print('how much painting I need')

# 1L = area of 2m²

width = float(input('What\'s the width? '))
height = float(input('What\'s the height? '))

area = width * height
result = area / 2

print('Dimensions: {} x {} || Area: {}m² || Ink needed: {}L'.format(width, 
height, 
area, 
result))

