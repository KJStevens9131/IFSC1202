file = open ("06.03 FTemps.txt")
a = 0
for i in file:
    far = open("06.03 CTempts.txt","a")
    cel = (float(i)-32)*(5/9)
    cel = round(cel,1)
    far.write(str(cel))
    far.write("\n")
    far.close()
    a = a + 1
print(str(a) + " record written")
    