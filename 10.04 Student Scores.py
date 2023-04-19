file = "10.04 StudentScores.txt"
print("{0}\t{1}\t        {2}\t       {3}\t     {4}\t  {5}\t".format("First", "Last", "ID", "Running", "Semester", "Letter"))
print("{0}\t{1}\t       {2}\t       {3}\t      {4}\t   {5}\t".format("Name", "Name", "Number", "Average", "Average", "Grade"))

class Student():
    def __init__(self, name1, name2, num, grades):
        self.FirstName = name1
        self.LastName = name2
        self.TNumber = num
        self.Grades = grades

    def RunningAverage(self):
        grades = []
        for grade in self.Grades:
            if grade != "": grades.append(int(grade))
            else:grades.append(0)
        return sum(grades) / len(grades)

    def TotalAverage(self):
        grades = []
        for grade in self.Grades:
            if grade!="":grades.append(int(grade))
        return sum(grades) / len(grades)
        
    def LetterGrade(self):
        average = self.RunningAverage()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

k = []
with open(file, "r") as infile:
    for line in infile:
        line = line.strip().split(",")
        s = Student(line[0], line[1], line[2], line[3:])
        k.append(s)
for i in k:
    print("{}\t{}\t{:>14}{:>15.2f}{:>15.2f}{:>10}".format(i.FirstName, i.LastName, i.TNumber,i.TotalAverage(),i.RunningAverage(),i.LetterGrade()))