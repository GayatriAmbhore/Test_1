l = int(input('Enter length:'))
b = int(input('Enter breadth:'))
r = int(input('Enter radius:'))

area = (l * b) + (3.14 * r * r/ 2)
perimeter = l + l + b + (3.14 * r)

print('Area is:', area)
print('Perimeter is:', perimeter)