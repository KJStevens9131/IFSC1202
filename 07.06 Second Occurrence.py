s = input("Enter a string: ")

index = s.find('f')
if index == -1:
    print("Zero f")
else:
    index = s.find('f', index + 1)
    if index == -1:
        print("One f")
    else:
        print(index)