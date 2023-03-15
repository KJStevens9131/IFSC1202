# Taking input as a values seperated by spaces from user
a = input("Enter Values Seperated by Spaces : ")

# Loading the values in the list
a_list = a.split()

# Finding the distinct values from the list
a_distinct = len(set(a_list))

# Printing the distinct values
print("Number of Distinct Elements : ", a_distinct)