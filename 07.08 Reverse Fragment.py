s = input("Enter a string: ")
firsth = -1
lasth = -1 

for i in range(len(s)):
    if s[i] == "h":
        if firsth == -1:
            firsth = i
        lasth = i

if firsth != lasth:
    print(s[:firsth] + s[firsth:lasth + 1][::-1] + s[lasth + 1:])
else:
    print(s)