inputl = list()
inp = input("Enter input numbers seperated by space: " ).split()
n = len(inp)
for i in range(n):
    inputl.append(int(inp[i]))

for i in range(n):
    count = 1

    for j in range(n):

        if inputl[i] == inputl[j] and i != j:
            count += 1

    if count == 1:
        print(inputl[i], end = " ")