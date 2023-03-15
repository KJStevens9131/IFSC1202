inputlist = list()

Input = input("Enter input numbers seperated by space \n" ).split()

# n will be length of input

n = len(Input)

for i in range(n):

#now converting str data type into int data type and

#appending them into inputlist

    inputlist.append(int(Input[i]))

for i in range(n):

    count = 1 #count for current element

    for j in range(n):

        if inputlist[i] == inputlist[j] and i != j:

            count += 1

    if count == 1:

        print(inputlist[i], end = " ") # end = " " to print all number in same line

# seperated by space