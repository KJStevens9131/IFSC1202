a = input()
for i in range(len(a)//2,len(a)):  # iterating from the half of the string to last 
    # this will for both even and odd because a//b will give half for even and ceiling for odd
    # in both the program will be correct as half will be in second string only
    print(a[i],end="")
for i in range(len(a)//2): # now printing the second half
    print(a[i],end="")