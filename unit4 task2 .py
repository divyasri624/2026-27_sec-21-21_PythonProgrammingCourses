
student = {
    "name": "Divya Sri",
    "age": 15,
    "course": "CSE"
}

# Display keys
print("Keys:", student.keys())

# Display values
print("Values:", student.values())

# Display items
print("Items:", student.items())

# Get a value
print("Name:", student.get("name"))

# Update dictionary
student.update({"age": 16})
print("Updated Dictionary:", student)

# Remove an item
student.pop("course")
print("After Pop:", student)
