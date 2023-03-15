# Reading input
s = input("Enter Values Separated by Space: ")

# Using split() function to split the input into list
lst = s.split(" ")

# Looping through each value in list
for x in range(len(lst)):

    # Checking x is odd
    if int(lst[x])%2==1:

        # Printing the value of x
        print(lst[x])