a = str(input("Enter a string: "))

if a.count("h") >= 2:
    print(a[:a.find("h")] + a[a.rfind("h") + 1:])
else:
    print(a.count("h"))