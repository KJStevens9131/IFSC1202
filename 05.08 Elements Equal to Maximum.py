large = 0
spawn = 0
while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0: 
        break
    if large < n:
        large = n
        spawn = 1
    elif large == n:
        spawn += 1
print("Maximum:", large)
print("Number of Occurrences:", spawn)