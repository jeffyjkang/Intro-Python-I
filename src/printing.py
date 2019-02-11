"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# for floats before decimal padding value represents length of complete output, after period limits number of positions after decimal
print('x is %(first)d, y is %(second).5f, z is %(third)s' %
      {'first': x, 'second': y, 'third': z})
# Use the 'format' string method to print the same thing
# you can also give placeholders an explicit positional index
print('x is {}, y is {}, z is {}'.format(x, y, z))
# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, z is {z}')
