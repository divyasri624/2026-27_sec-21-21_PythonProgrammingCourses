subjects = {
    "Maths": 90,
    "Physics": 85,
    "Chemistry": 88,
    "English": 92
}

print("Subject Names:")
for key in subjects.keys():
    print(key)

print("\nMarks:")
for value in subjects.values():
    print(value)

print("\nSubject and Marks:")
for key, value in subjects.items():
    print(key, ":", value)