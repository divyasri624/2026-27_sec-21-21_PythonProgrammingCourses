# Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print("Squares:", squares)
print("Even Numbers:", even_numbers)