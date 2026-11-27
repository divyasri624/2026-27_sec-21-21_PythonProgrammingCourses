numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter list index: "))
    print("Element:", numbers[index])

except ValueError:
    print("Invalid input! Enter an integer.")

except IndexError:
    print("Invalid index! Index is out of range.")