#prints the name for each column and opens/names the text files
print("{:15s}{:15s}{:12s}{:16s}{:13s}{:10s}".format("First Name", "Last Name", "ID Number", "Hours Worked","Hourly Wage", "Weekly Pay"))
employeesFile = "11.02 Employees.txt"
timeFile = "11.02 Hours.txt"
j = open(employeesFile)
emp = []
#start of clas and operations
class Employee:
    def __init__(self, FirstName, LastName, IdNumber, Wage, HoursWorked = 0):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IdNumber = int(IdNumber)
        self.HoursWorked = float(HoursWorked)
        self.Wage = float(Wage)

    def WeeklyPay(self):
        if self.HoursWorked > 40:
            return self.Wage*40+self.Wage*1.5*(self.HoursWorked-40)
        return self.HoursWorked*self.Wage

def find_employee(emp : Employee, idnum):
    for i in range(len(emp)):
        if idnum == emp[i].IdNumber:
            return i
    return -1

for i in j:
    i = i.strip("\n").split(",")
    FirstName, LastName, IdNumber, Wage = i[0], i[1], int(i[2]), float(i[3])
    emp2 = Employee(FirstName, LastName, IdNumber, Wage)
    emp.append(emp2)

#opens hours file and puts into J
j = open(timeFile)

for i in j:
    i = i.split(",")
    IdNumber, hours = int(i[0]), float(i[1])
    index = find_employee(emp, IdNumber)
    if index != -1:
        emp[index].HoursWorked = hours

#outputs the final sections of data
for emp in emp:
    print("{:13s}  {:12s}{:10d}{:14}{:14}{:14.2f}".format(emp.FirstName, emp.LastName, emp.IdNumber,emp.HoursWorked, emp.Wage, emp.WeeklyPay()))