a = [int(j) for j in input("Enter Values Seperated by Spaces: ").split()]
b = 0
for i in range(1,len(a)-1):
    if a[i - 1] < a[i] > a[i + 1]:
        b += 1
print(b)