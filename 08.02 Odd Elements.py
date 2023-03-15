a = input("Enter Values Separated by Space: ")
b = a.split(" ")
for x in range(len(b)):
    if int(b[x])%2==1:
        print(b[x])