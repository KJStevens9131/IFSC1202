def find_row(s):
    first=[]
    for i in range(s):
        if i==0 or i==s-1:
            first.append('+')
        else:
            first.append('-')
    return first        
        
n=int(input("Enter Size:"))
s=n+2
l=[]
l.append(find_row(s))

for i in range(1,s-1):
    c=[]                
    for j in range(s):
        if j==0 or j==s-1:
            c.append('|')
        else:
            if(i%2==0): 
                if(j%2==0):
                    c.append(' ')
                else:
                    c.append('*')
            else:
                if(j%2==0):
                    c.append('*')
                else:
                    c.append(' ')   
                    
    l.append(c)
l.append(find_row(s))  
a=""
for i in range(s):
    a+=''.join(l[i])        
    a+='\n'                 
print(a)