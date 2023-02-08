num = int(input("Enter A 4 Digit Number: "))
ones = (int(num)%10)
tens = (int(num)%100)//10
hundreds = (int(num)%1000)//100
thousands = (int(num)//1000)

if thousands < hundreds and thousands < tens and thousands < ones and hundreds < tens and hundreds < ones and tens < ones :
    print("YES")
else:
    print("NO")