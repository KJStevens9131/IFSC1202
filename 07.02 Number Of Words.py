def space(s):
    a = 0
    for i in range(0, len(s)):      
        if s[i] == " ":
            a += 1        
    return a
s = input("Enter your sentence: ")
print(space(s)+1, "words")