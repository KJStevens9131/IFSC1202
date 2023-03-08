a = input("Enter a string: ")
index = a.find('f')
if index == -1:
    print("Zero f")
else:
    index = a.find('f', index + 1)
    if index == -1:
        print("One f")
    else:
        print(index)