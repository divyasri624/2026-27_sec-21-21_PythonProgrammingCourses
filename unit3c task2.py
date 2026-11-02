# Creating a set
s = {10, 20, 30, 40}

print("Original set:", s)

# Membership testing
print("20 in set:", 20 in s)
print("50 in set:", 50 in s)

# add() method
s.add(50)
print("After adding 50:", s)

# remove() method
s.remove(30)
print("After removing 30:", s)

# discard() method
s.discard(40)
print("After discarding 40:", s)