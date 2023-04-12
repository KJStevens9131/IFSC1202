#opens file and then take the first two lines
Carfile = open("10.03 Cars.txt","r")
mkml=Carfile.read()
mkml2=mkml.split("\n")
#class
class CarType: 
    def __init__(self, model, year):
            self.Make = model
            self.Year = year
            self.Speed = 0 
    def Accelerate(self,value):
        self.Speed = self.Speed + value
    def Brake(self,value):
        self.Speed = self.Speed - value

def changeAndSpeed(speed,change):
    print("")
    print("Change Speed")
    for i in speed:
        print(i,end="{:>5s}".format("\t"))
        if i>0: 
            change.Accelerate(i)
        else:
            i=i*(-1)
            change.Brake(i) 

        print(change.Speed) 
mm=mkml2[0].split(",")
makeModel=[]
speed=[]
for k in mm:
    makeModel.append(k)

model=makeModel[0] 
make=makeModel[1] 

for k in range(1,len(mkml2)):
    speed.append(int(mkml2[k])) 
change=CarType(model,make)
#final output
print("Make: ",change.Make) 
print("Year: ",change.Year) 

changeAndSpeed(speed,change) 