t = str(input("Enter the string: "))

if t.count("h") >= 2:

    print(t[:t.find("h")] + t[t.rfind("h") + 1:])

else:

    print(t.count("h"))