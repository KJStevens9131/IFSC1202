a = int(input("Enter A: "))
b = int(input("Enter B: "))
for c in range(a, b + 1):
   # all prime numbers are greater than 1
    if c > 1:
        for i in range(2, c):
           if (c % i) == 0:
               break
        else:
           print(c)