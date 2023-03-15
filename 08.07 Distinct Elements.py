a = input("Enter Values Seperated by Spaces : ")
b = a.split()
c = len(set(b))
print("Number of Distinct Elements : ", c)