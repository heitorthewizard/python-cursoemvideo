from simple_colors import *

print('Eletronic Radar')
speed = float(input('Car\'s speed: '))

if speed > 80:
    extra_speed = speed - 80
    traffic_ticket = format((extra_speed * 7), '.2f')
    print(red(f'''
    Your traffic ticket is R${traffic_ticket} for breaking the speed limit
    limit: 80Km/h
    your speed: {speed}Km/h
    '''))
else:
    print(green('Well Done, your under the speed limit'))

