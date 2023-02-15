large = 0
index = 0
index2 = 0
while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0: 
        break
    index+=1
    if large < n:
        large = n
        large,index2 = n,index
print("Maximum:", large)
print("Index: ", index2)