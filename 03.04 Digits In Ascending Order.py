num = int(input("Enter A 3 Digit Number: "))
ones = (int(num)%10)
tens = (int(num)%100)//10
hundreds = (int(num)//100)

if hundreds < tens and hundreds < ones and tens < ones :
    print("YES")
else:
    print("NO")