name = "raghav"
print(len(name))

x = int(input("Enter a number: "))
a = 0
b = 1
for i in range(x):
    print(a, end=" ")
    c = a + b
    a = b
    b = c