num = input("Enter A 3 Digit Number: ")
ones = (int(num)%10)
tens = (int(num)%100)//10
hundreds = (int(num)//100)
print("Reverse of Digits: {}{}{}".format(ones, tens, hundreds))