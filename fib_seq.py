a = 0
b = 1

num = int(input("Please enter a number: "))

while a <= num:
    print(a)
    c = a + b
    a = b
    b = c

print("\nEnd")
