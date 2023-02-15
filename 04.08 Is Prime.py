n = int(input("Enter a number greater than 1: "))
for i in range(2, n):
        if (n % i) == 0:
            print("COMPOSITE")
        else:
            print("PRIME")
        break