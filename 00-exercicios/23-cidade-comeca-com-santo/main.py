from simple_colors import *

city_name = input('Enter a city name: ').strip().lower()
splitted_city_name = city_name.split()
first_name = splitted_city_name[0]

if first_name.find('santo') == 0:
    print(green('It starts with Santo'))
else:
    print(red('It doesn\'t start with Santo'))
