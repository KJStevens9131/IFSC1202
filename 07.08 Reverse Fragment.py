s = input("Enter a string: ")
first_h = -1
last_h = -1
for i in range(len(s)):
    if s[i] == 'h':
        if first_h == -1:
            first_h = i
        last_h = i

if first_h != last_h:
    print(s[:first_h] + s[first_h:last_h + 1][::-1] + s[last_h + 1:])
else:
    print(s)