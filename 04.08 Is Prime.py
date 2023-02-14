n = int(input("Enter N: "))

for i in range(2, n):
        if (n % i) == 0:
            print("COMPOSITE")
        else:
            print("PRIME")
        break