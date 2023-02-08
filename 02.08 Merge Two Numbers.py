num = input("Enter First 2 Digit Number: ")
ones = (int(num)%10)
tens = (int(num)%100)//10
num = input("Enter Second 2 Digit Number: ")
ones2 = (int(num)%10)
tens2 = (int(num)%100)//10
print("Merged Number: {}{}{}{}".format(tens, tens2, ones, ones2))