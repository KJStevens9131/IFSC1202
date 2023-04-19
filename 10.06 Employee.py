payFile = open("10.06 Payroll.txt")
print("First Last Id      Hours  Hourly Weekly")
print("Name  Name Number  Worked Wage   Pay")

class Employee:
    def __init__(self, name1, name2, num, hours, pay):
        self.FirstName1 = name1
        self.LastName1 = name2
        self.IDNumber1 = num
        self.HoursWorked = hours
        self.Wage1 = pay 

    def WeeklyPay(self):
        if(self.hours <= 40):
            weekly_pay = self.hours * self.pay
        else:  
            weekly_pay = (self.pay*40) + (self.pay*1.5*(self.hours-40))
        return weekly_pay

    def __repr__(self):
        return (self.name1, self.name2, self.num, self.hours, self.pay, self.WeeklyPay())

employee=[]

for i in payFile.readlines():
    i = i.split(",")
    employee = Employee(i[0], i[1], i[2], i[3], i[4])
    for k in range(1,len(i)):
        employee.append(int(i[k]))
    print(employee.name1, employee.name2, employee.num, employee.hours, employee.pay, employee.WeeklyPay())