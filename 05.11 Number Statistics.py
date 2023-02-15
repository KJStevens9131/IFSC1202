program = True
count = 0
summ = 0
valuelow = 9999
valuehigh = -9999
while program:  
    n = float(input("Enter a Value (zero to quit): "))
    if n == 0:
        program = False
        break

    count += 1
    summ += n

    if n <= valuelow:
        valuelow = n
    if n >= valuehigh:
        valuehigh = n

if count != 0:
    print("{:<8} {}".format("Count:",count))
    print("{:<8} {}".format("Sum:",summ))
    print("{:<8} {}".format("Average:",summ/count))
    print("{:<8} {}".format("Minimum:",valuelow))
    print("{:<8} {}".format("Maximum:",valuehigh))