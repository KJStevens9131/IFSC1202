# Python program
# Input string containing values
values = input("Enter Values Seperated by Spaces: ")
# Split string the value seperated space and store in list
lst = values.split(' ')
# Loop to check list element
for i in range(0,len(lst)):
    # If current element is not last element because when current element is last then next element is not possible
    if i<len(lst)-1:
        # If next element is greater than current element
        if int(lst[i+1])>int(lst[i]):
            # Then print next element
            print(int(lst[i+1]))