students = {
    1: {"name": "Divya", "marks": 90},
    2: {"name": "Priya", "marks": 85},
    3: {"name": "Ravi", "marks": 95}
}

print("Student Details:")

for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()