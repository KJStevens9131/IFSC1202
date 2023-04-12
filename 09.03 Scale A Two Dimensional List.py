def plist(a):
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()

def slist(a,s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=s*a[i][j]
    return a

ins = open("09.03 NumbersList.txt", "r")
a = []
for line in ins:
    number_strings = line.split()
    numbers = [int(n) for n in number_strings] 
    a.append(numbers)
print_list(a)
s=int(input("Enter the scalar value : "))
a=scale_list(a,s)
print_list(a)