dict1 = {"Maths": 90, "Physics": 85}
dict2 = {"Chemistry": 88, "English": 92}

# Create a copy of the first dictionary
merged = dict1.copy()

# Merge the second dictionary
merged.update(dict2)

print("Original Dictionary 1:", dict1)
print("Original Dictionary 2:", dict2)
print("Merged Dictionary:", merged)