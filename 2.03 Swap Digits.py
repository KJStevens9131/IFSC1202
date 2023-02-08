num = input("Enter A Number: ")
firstdig = (int(num)//10)
lastdig = (int(num)%10)
print("Swapped Number {}{}".format(lastdig, firstdig))