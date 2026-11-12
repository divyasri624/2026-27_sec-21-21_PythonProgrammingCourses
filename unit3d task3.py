def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))

t, avg = calculate(a, b, c)

print("Total Marks =", t)
print("Average =", avg)