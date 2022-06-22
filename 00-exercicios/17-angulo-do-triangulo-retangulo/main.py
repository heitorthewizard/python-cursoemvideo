from math import radians, sin, cos, tan

while True:
    angle = float(input('Give the angle value: '))

    if angle > 360 or angle < 0:
        print('wrong input. Angle: 0 - 360⁰')
    else:
        break

# convert angle to radian
radian_angle = radians(angle)

# getting the result of each one
sin = sin(radian_angle)
cos = cos(radian_angle)
tan = tan(radian_angle)

print('''
    The Result:
    angle: {:.2f}
    angle in radians: {:.2f}
    sin: {:.2f}
    cos: {:.2f}
    tan: {:.2f}
'''.format(angle, radian_angle, sin, cos, tan))
