n = int(input("Enter N: "))
num = 0
result = 0
for i in range(1, n + 1):
    num = int(input("Enter A Number: "))
    if num == 0:
        result = result + 1
print(result)
