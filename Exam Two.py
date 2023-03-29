import csv
datafile = open('Exam Two Properties.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
for row in datareader:
    data.append(row) 
print("Street                    City        State Zip     Price") 
print (data) 
zip = input("Please enter a zip code: ")

#I know the project isnt finished but I was having difficulty with the list and then ran out of time to work on other aspects 
