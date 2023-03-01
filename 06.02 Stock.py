inputFile = open("06.02 Stock.txt","r")
a = inputFile.read()
a = [float(i) for i in a.split()]

print("Price     Change")
print(a[0])

for i in range(1, len(a)):
    percentage = ((a[i]-a[i-1])/a[i-1])*100
    print ("{:.2f}     {:+.2f}%".format(a[i],percentage))