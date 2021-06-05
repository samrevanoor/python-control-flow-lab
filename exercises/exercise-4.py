# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = input('''Enter the lengths of three side of a triangle: 
a: ''')
b = input('b: ')
c = input('c: ')

if a == b == c:
    print(f'A triangle with sides of {a}, {b} & {c} is an equilateral triangle')
elif a == b != c or a != b == c or a == c != b:
    print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')
else:
    print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
