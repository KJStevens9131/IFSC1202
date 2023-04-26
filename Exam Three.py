#Things to state to make the program run and look nice
import math
print("{:20s}{:12s}{:12s}{:10s}{:14s}{:10s}{:12s}{:12s}{:12s}".format("Type", "Side 1", "Side 2", "Side 3","Perimeter", "Area","Angle 1","Angle 2","Angle 3"))
j = open("Exam Three Triangle.txt", "r")
items = []
pi = 3.1415926535

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

#Identify the type of triangle
    def Type(self):
        if(self.s1==self.s2 and self.s2==self.s3):
            return "Equilateral"
        elif(self.s1==self.s2 or self.s2==self.s3 or self.s3==self.s1):
            return "Isocelese"
        else:
            return "Scalene"

#Adds the sides to find the perimeter
    def Perimeter(self):
        return self.s1+self.s2+self.s3

#Based on the type of triangle it will find the different areas
    def Area(self):
        if(self.Type()=="Equilateral"):
            return ((3**(1/2))/4)*(self.s1*self.s1)

        elif(self.Type()=="Isocelese"):
            if(self.s1==self.s2):
                x=self.s1
                y=self.s3
            else:
                x=self.s1
                y=self.s2
            return (y*((4*x*x)-(y*y))**(1/2))/4

        else:
            k=self.Perimeter()/2
            return (k*(k-self.s1)*(k-self.s2)*(k-self.s3))**(1/2)

#Based on the type of triangle it will find the different Angles
    def Angles(self):
        if(self.Type()=="Equilateral"):
            return [60,60,60]

        elif(self.Type()=="Isocelese"):
            if(self.s1==self.s2):
                y=self.s3
                #selgna is angles backwards just so the word angles isnt used too much
                selgna = ((self.s1**2)-((y/2)**2))**(1/2)
                Angle1=(math.acos((y/2*y/2+self.s1*self.s1-selgna*selgna)/(y*self.s1)))*180/pi;
                Angle2=Angle1
                Angle3=180-Angle1-Angle2

                return [Angle1,Angle2,Angle3]

            elif(self.s2==self.s3):
                y=self.s1
                selgna=((self.s2**2)-((y/2)**2))**(1/2)
                Angle1=(math.acos((y/2*y/2+self.s2*self.s2-selgna*selgna)/(y*self.s2)))*180/pi;
                Angle2=Angle1
                Angle3=180-Angle1-Angle2

                return [Angle1,Angle2,Angle3]

            else:
                y=self.s2
                selgna=((self.s1**2)-((y/2)**2))**(1/2)
                Angle1=(math.acos((y/2*y/2+self.s1*self.s1-selgna*selgna)/(y*self.s1)))*180/pi;
                Angle2=Angle1
                Angle3=180-Angle1-Angle2

                return [Angle1,Angle2,Angle3]

        else:
            y=self.s3
            selgna = 2*(self.Area()/y)
            angle1=math.sqrt(math.pow(self.s1,2) - math.pow(selgna,2))
            angle2=y-angle1
            Angle1=(math.acos((angle1*angle1+self.s1*self.s1-selgna*selgna)/(2*angle1*self.s1)))*180/pi;
            Angle2=(math.acos((angle2*angle2+self.s2*self.s2-selgna*selgna)/(2*angle2*self.s2)))*180/pi;
            Angle3=180-Angle1-Angle2

            return [Angle2, Angle1, Angle3]

for i in j:
    num = i.split(',')
    s1 = float(num[0])
    s2 = float(num[1])
    s3 = float(num[2])
    items.append(Triangle(s1,s2,s3))

#Outputs the data
for final in items:
    print("{:12s}{:14.3f}{:12.3f}{:12.3f}{:12.3f}{:10.3f}{:13.3f}{:12.3f}{:12.3f}".format(final.Type(), final.s1, final.s2,final.s3, final.Perimeter(), final.Area(),final.Angles()[0],final.Angles()[1],final.Angles()[2]))