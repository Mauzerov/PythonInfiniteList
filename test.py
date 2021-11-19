from infinite import InfList

x = InfList()

print(x)

x[0] = 5
x[1] = 6
print(x)
x[0][0] = [2139, 23, 24, 23]
print(x)
print(x[0] + [1, 2, 3])
