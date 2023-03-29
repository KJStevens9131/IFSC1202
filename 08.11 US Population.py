listp = []
listc = [0]
listpe = [0]
file = open('08.11 USPopulation.txt','r')

for i in file:
    listp.append(int(i)*1000)
file.close()

for i in range(41):
    if(i>=1):
        a = listp[i]-listp[i-1]
        listc.append(a)
        b = round((a/listp[i-1])*100,2)
        listpe.append(b)
j=0

print("Year\t\tPopulation\t\tChange\t\tPercent Change")

for year in range(1950,1991):
    if(j==0):
        print(year,"\t\t",listp[j],"\t\t","N/A","\t\t","N/A")
    else:
        print(year,"\t\t",listp[j],"\t\t",listc[j],"\t",str(listpe[j])+"%")
    j+=1

average=sum(listc)/41
print("Average Change: ",a)
maxx=listc[1]
minn=listc[1]
maxi=0
mini=0

for i in range(2,len(listc)):
    if(listc[i]>maxx):
        maxx=listc[i]
        maxi=i
    if(listc[i]<minn):
        minn=listc[i]
        mini=i
print("Minimum Change: ",minn," (",1950+mini,")")
print("Maximum Change: ",maxx," (",1950+maxi,")")