a = input("Enter values separated by spaces: ").split()   # read data

for i in range(0, len(a), 2):
    if i+1 < len(a):
        a[i], a[i+1] = a[i+1], a[i]
print("Swapped Values: ", end="")

for j in a:
    print(j, end=" ")
print()