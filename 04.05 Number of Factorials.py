n = int(input("Enter N: "))
num = 1
result = 0
for i in range(1, n + 1):
    num = num * i
    result = result + num
print("Sum of Factorials: ", result)