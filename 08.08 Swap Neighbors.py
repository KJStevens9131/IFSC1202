lst = input("Enter values separated by spaces: ").split()   # read data

# swap all pairs
for i in range(0, len(lst), 2):
    if i+1 < len(lst):
        lst[i], lst[i+1] = lst[i+1], lst[i]

# print result
print("Swapped Values: ", end='')
for item in lst:
    print(item, end=' ')
print()