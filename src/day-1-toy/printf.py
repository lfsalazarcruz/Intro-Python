x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
"x is %d" %10 + ", y is %d" %2.25 + ", z is %s" %"I like turtles!"


# Use the 'format' string method to print the same thing
f"x is {x}, y is {y}, z is {z}";