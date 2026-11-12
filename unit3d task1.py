def rectangle(l, b):
    area = l * b
    perimeter = 2 * (l + b)
    return area, perimeter

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

a, p = rectangle(l, b)

print("Area =", a)
print("Perimeter =", p)