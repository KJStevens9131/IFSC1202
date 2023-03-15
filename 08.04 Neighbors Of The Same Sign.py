c=input("enter values seprated by space =")
l1=c.split()
l1=[int(i) for i in l1]
n=len(l1)
for i in range(n-1):
    if l1[i]>0 and l1[i+1]>0:
        print(l1[i],l1[i+1])
    elif l1[i]<0 and l1[i+1]<0:
        print(l1[i],l1[i+1])