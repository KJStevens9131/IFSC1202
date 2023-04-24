#some pieces are missing because I used the panda elements on a different program 
# but I cannont find them in gitpod so i had to change the code 
print("{:15s}{:15s}{:12s}{:16s}{:13s}{:10s}{:10s}".format("First Name", "Last Name", "T-Number", "Course","Name", "Room","Meeting Times"))
RegFile = "11.03 Registration.txt"
studentFile = "11.03 Students.txt"
j = open(RegFile)
k = open(studentFile)

class Student:
    def __init__(self, FirstName, LastName, TNumber):
        self.FirstName = FirstName
        self.LastName = LastName
        self.TNumber = TNumber
        self.CourseList = []

class StudentList:
    def __init__(self):
        self.SList = []

    def add_student(self, FirstName, LastName, TNumber):
        student = Student(FirstName, LastName, TNumber)
        self.SList.append(student)

    def find_student(self, student_to_find) -> int:
        for index, student in enumerate(self.SList):
            if student.TNumber == student_to_find:
                return index
        return -1 

    def print_studentList(self):
        data = DataFrame([vars(f) for f in self.SList])


    def add_student_from_file(self, file_Name):
        data = read_csv(file_Name, Names=["FirstName", "LastName", "TNumber"])


class Course:
    def __init__(self, Department, Number, Name, Room, MeetingTimes):
        self.Department = Department
        self.Number = Number
        self.Name = Name
        self.Room = Room
        self.MeetingTimes = MeetingTimes


class CourseList:
    def __init__(self):
        self.CourseList = []

    def add_course(self, Department, Number, Name, Room, MeetingTimes):
        self.CourseList.append(Course(Department, Number, Name, Room, MeetingTimes))

    def find_course(self, depart, num) -> int:
        for index, course in enumerate(self.CourseList):
            if course == depart and Number == num:
                return index
        return -1

    #def add_course_from_file(self, file_Name):