import csv
#declaring the varibales
city_dict = {}
city_tuple = ()
#opening the csv file
with open('Exam Two Properties.csv') as csvfile:
    #reading the file
    reader = csv.DictReader(csvfile)
    for row in reader:
        #creating the dictionary
        city_tuple = (row['city'], row['State'])
        city_dict[city_tuple] = row['Population']
#displaying the dictionary
for key, value in city_dict.items():
    print(key[0],key[1],value)
#taking inputs
city = input("Please enter a city: ")
state = input("Please enter a state: ")
#displaying output
if (city,state) in city_dict:
    print(city,state," has a population of ",city_dict[(city,state)])
else:
    print("Data is not exist")