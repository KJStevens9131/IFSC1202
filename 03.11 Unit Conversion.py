num = input("Enter From Value: ")
fromunit = input("Enter From Unit (in, ft, yd, mi): ")
tounit = input("Enter To Unit (in, ft, yd, mi): ")

#inch conversion
if fromunit == "in" and tounit == "ft":
    fin = (float(num) / 12)
    fin2 = round(float(fin),7)
    print(num, "in", "=>", fin2, "ft")
elif fromunit == "ft" and tounit == "in":
    fin = (float(num) * 12)
    fin2 = round(float(fin),7)
    print(num, "ft", "=>", fin2, "in")


elif fromunit == "in" and tounit == "yd":
    fin = (float(num) / 36)
    fin2 = round(float(fin),7)
    print(num, "in", "=>", fin2, "yd")
elif fromunit == "yd" and tounit == "in":
    fin = (float(num) * 36)
    fin2 = round(float(fin),7)
    print(num, "yd", "=>", fin2, "in")

elif fromunit == "in" and tounit == "mi":
    fin = (float(num) / 63360)
    fin2 = round(float(fin),7)
    print(num, "in", "=>", fin2, "mi")
elif fromunit == "mi" and tounit == "in":
    fin = (float(num) * 63360)
    fin2 = round(float(fin),7)
    print(num, "mi", "=>", fin2, "in")

#feet conversion
elif fromunit == "ft" and tounit == "yd":
    fin = (float(num) / 3)
    fin2 = round(float(fin),7)
    print(num, "ft", "=>", fin2, "yd")
elif fromunit == "yd" and tounit == "ft":
    fin = (float(num) * 3)
    fin2 = round(float(fin),7)
    print(num, "yd", "=>", fin2, "ft")

elif fromunit == "ft" and tounit == "mi":
    fin = (float(num) / 5280)
    fin2 = round(float(fin),7)
    print(num, "ft", "=>", fin2, "mi")
elif fromunit == "mi" and tounit == "ft":
    fin = (float(num) * 5280)
    fin2 = round(float(fin),7)
    print(num, "mi", "=>", fin2, "ft")

#yard conversion
elif fromunit == "yd" and tounit == "mi":
    fin = (float(num) / 1760)
    fin2 = round(float(fin),7)
    print(num, "yd", "=>", fin2, "mi")
elif fromunit == "mi" and tounit == "yd":
    fin = (float(num) * 1760)
    fin2 = round(float(fin),7)
    print(num, "mi", "=>", fin2, "yd")


else:
    print("The From Unit or To Unit is not valid")