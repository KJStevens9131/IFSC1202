large = 0
while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0: 
        break
    if large < n:
        large = n
print("Maximum:", large)