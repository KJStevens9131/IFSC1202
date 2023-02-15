n = 1
prev = 0
c = 0
a = 0
program = True
while program:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0:
        program = False
        break
    if n != 0:
        if a == 0:
            prev = n
        if n > prev:
            c += 1
        a += 1
        prev = n
print("Number of Values Greater Than the Previous:", c)