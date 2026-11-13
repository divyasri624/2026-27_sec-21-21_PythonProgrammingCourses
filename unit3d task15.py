from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using map()
print("Squares:", list(map(lambda x: x*x, numbers)))

# Using filter()
print("Even numbers:", list(filter(lambda x: x%2 == 0, numbers)))

# Using reduce()
print("Sum:", reduce(lambda x, y: x+y, numbers))