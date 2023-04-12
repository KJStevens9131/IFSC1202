class Pet ():

	def __init__(self):
		self.Name = ""
		self.Type = ""
		self.Age = 0
	def __repr__(self):
		return"{:>s}\t{:>s}\t{:>s}".format(self.Name,self.Type,self.Age)

print("{:>s}{:>9s}{:>7s}".format("Name", "Type", "Age"))
firstAnimal = Pet()
secondAnimal = Pet()
thirdAnimal = Pet()
petfile = open("10.01 Pets.txt","r")

x = petfile.readline()
y = x.strip().split(",")
firstAnimal.Name = y[0]
firstAnimal.Type = y[1]
firstAnimal.Age = y[2]
print(firstAnimal)

x = petfile.readline()
y = x.strip().split(",")
secondAnimal.Name = y[0]
secondAnimal.Type = y[1]
secondAnimal.Age = y[2]
print(secondAnimal)

x = petfile.readline()
y = x.strip().split(",")
thirdAnimal.Name = y[0]
thirdAnimal.Type = y[1]
thirdAnimal.Age = y[2]
print(thirdAnimal)

petfile.close()