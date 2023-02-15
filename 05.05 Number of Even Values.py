even = 0
n=1
while n != 0:
    n = int(input("Enter a Number (zero to quit): "))
    if n % 2 == 0: 
        even += 1
print("Number of Even Values:", even)