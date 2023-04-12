def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
                       print(a[i][j],end=' ')
        print('\n')

def swap_columns(a,i,j):
    for k in range(len(a)):
        l=a[k][i]
        a[k][i]=a[k][j]
        a[k][j]=l

k=open('09.02 NumbersList.txt')
a=k.readlines()
a=''.join(a)
a=a.split('\n')
for i in range(len(a)):
    a[i]=a[i].split(' ')
    a[i]=map(int,a[i])
    a[i]=list(a[i])
print_list(a) 

i,j=input('Enter the columns to swap: ').split()
i=int(i)
j=int(j)
swap_columns(a,i,j) 
print_list(a)