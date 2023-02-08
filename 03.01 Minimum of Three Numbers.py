x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
if x < y and x < z :
    print(x)
elif y < x and y < z:
    print(y)
else:
    print(z)