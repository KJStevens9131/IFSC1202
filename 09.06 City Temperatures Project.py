with open("09.06 CityTemps.txt", 'r') as file:
    t2 = []
    l = file.readline()

    while l:
        row = l.split()
        t2.append(row)
        l = file.readline()

for i in range(len(t2)):
    tot = 0    
    for t1 in t2[i][1:]:
        tot = tot + float(t1)
    a = tot / (len(t2[i]) - 1)
    t2[i].append(int(a))

print(f"{'City':<10}{'Mo':<10}{'Tu':<10}{'We' : <10}{'Th' : <10}{'Fr' : <10}{'Sa' : <10}{'Su' : <10}{'Avg' : <10}")

for i in range(len(t2)):
    for j in range(len(t2[0])):
        print(f"{t2[i][j] : <10}", end='')
    print("")