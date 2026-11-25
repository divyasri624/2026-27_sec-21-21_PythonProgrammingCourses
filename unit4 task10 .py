students = [
    {"name": "Divya", "marks": 90},
    {"name": "Priya", "marks": 75},
    {"name": "Ravi", "marks": 85},
    {"name": "Kiran", "marks": 95}
]

# Sort in ascending order
ascending = sorted(students, key=lambda x: x["marks"])

# Sort in descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
for student in ascending:
    print(student)

print("\nDescending Order:")
for student in descending:
    print(student)