list_population=[]
list_change=[0]
list_percent=[0]
#reading file and populating to list
file=open('08.11 USPopulation.txt','r')
for i in file:
    list_population.append(int(i)*1000)
file.close()
#calculating change and percent change
for i in range(41):
    if(i>=1):
        change=list_population[i]-list_population[i-1]
        list_change.append(change)
        percent_change=round((change/list_population[i-1])*100,2)
        list_percent.append(percent_change)
j=0
#printing the values in given format
print("Year\t\tPopulation\t\tChnage\t\tPercent Change")
for year in range(1950,1991):
    if(j==0):
        print(year,"\t\t",list_population[j],"\t\t","N/A","\t\t","N/A")
    else:
        print(year,"\t\t",list_population[j],"\t\t",list_change[j],"\t",str(list_percent[j])+"%")
    j+=1
#finding the average max and min change and year
average=sum(list_change)/41
print("Average population change: ",change)
maxi=list_change[1]
mini=list_change[1]
max_index=0
min_index=0
for i in range(2,len(list_change)):
    if(list_change[i]>maxi):
        maxi=list_change[i]
        max_index=i
    if(list_change[i]<mini):
        mini=list_change[i]
        min_index=i
print("Maximum change and year: ",maxi,1950+max_index)
print("Minimum change and year: ",mini,1950+min_index)