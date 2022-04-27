num = int(input("Please enter a number: "))

def fibonacci(a, b):
    print(a)

    c = a + b
    a = b
    b = c

    if a <= num:
        fibonacci(a, b)



fibonacci(0, 1)

print("\nEnd")