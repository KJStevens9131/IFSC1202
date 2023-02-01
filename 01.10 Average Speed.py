kilo = input("Enter kilometers: ")
min1 = input("Enter Minutes: ")
sec1 = input("Enter Seconds: ")
time = (float(min1) + (float(sec1)/60))/60
miles = (float(kilo) / 1.61)
final = (float(miles)/float(time))
print (float(final))