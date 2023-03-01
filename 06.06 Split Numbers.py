num2 = 0
odd = 0
even = 0
prime = 0
 
inputFile = open("06.06 Numbers.txt","r")
evenFile = open("06.06 Evennumbers.txt","w+")
oddFile = open("06.06 Oddnumbers.txt","w+")
primeFile = open("06.06 Primenumbers.txt","w+")

def isEven(num):
    return num % 2 == 0   
def isOdd(num):
    return num % 2 != 0   
def isPrime(num):
    prim = False

    if(num == 1):
        return False
    elif num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                prim = True
                break

    return (not prim)

for line in inputFile:
    line = int(line.strip())
    num2 += 1

    if isEven(line):
        evenFile.write(str(line) + "\n")
        even += 1

    elif isOdd(line):
        oddFile.write(str(line) + "\n")
        odd += 1

    if isPrime(line):
        primeFile.write(str(line) + "\n")
        prime += 1

print(even,"even numbers")
print(odd,"odd numbers")
print(prime,"prime numbers")
print(num2,"number read")

inputFile.close()        
evenFile.close()
oddFile.close()
primeFile.close()