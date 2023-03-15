a = input("Enter Values Seperated by Spaces: ")
b = a.split()
b = [int(i) for i in b]
c = len(b)
for i in range(c-1):
    if b[i] > 0 and b[i+1] > 0:
        print(b[i],b[i+1])
    elif b[i] < 0 and b[i+1] < 0:
        print(b[i],b[i+1])