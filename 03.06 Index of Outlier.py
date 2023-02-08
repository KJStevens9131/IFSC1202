x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
#x
if x == y and x!=z :
    print(3)
elif x == z and x!=y:
    print(2)
#y
elif y == x and y!=z:
    print(3)
elif y == z and y!=x:
    print(1)
#z
elif z == x and z!=y:
    print(2)
elif z == y and z!=x:
    print(1)
