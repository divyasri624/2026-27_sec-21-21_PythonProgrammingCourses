
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print("Addition:")
for i in range(2):
    print([a[i][j] + b[i][j] for j in range(2)])

print("Subtraction:")
for i in range(2):
    print([a[i][j] - b[i][j] for j in range(2)])

print("Multiplication:")
for i in range(2):
    print([sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)])
