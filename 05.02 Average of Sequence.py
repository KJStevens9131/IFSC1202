summ = 0
c = 0
while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0: 
        break
    summ += n
    c += 1
if c == 0:
    print("Sequence Length is 0")
else:
    print("Average:", summ / c)