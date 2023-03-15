a = input("Enter Values Seperated by Spaces: ")
b = a.split(' ')

for i in range(0,len(b)):
    if i<len(b)-1:
        if int(b[i+1])>int(b[i]):
            print(int(b[i+1]))