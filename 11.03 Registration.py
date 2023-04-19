#import pandas as pd


class Student:

    def __init__(self, first_name, last_name, t_number):
        self.first_name = first_name
        self.last_name = last_name
        self.t_number = t_number
        self.course_list = []


class StudentList:

    def __init__(self):
        self.student_list = []

    def add_student(self, first_name, last_name, t_number):
        student = Student(first_name, last_name, t_number)
        self.student_list.append(student)

    def find_student(self, student_to_find) -> int:
        for index, student in enumerate(self.student_list):
            if student.t_number == student_to_find:
                return index
        return -1  # can be any default value, but -1 reminds me of the default search function

    def print_student_list(self):
        # this statement gets all the variables associated with every
        # student object and parses it to a pandas data frame
        df = pd.DataFrame([vars(f) for f in self.student_list])
        print(df.to_string(index=False))  # make use of the pandas library to do pretty printing

    def add_student_from_file(self, file_name):
        # read_csv function obtains the data (in csv format) and makes it so it
        # can be used as a convenient python object
        df = pd.read_csv(file_name, names=["first_name", "last_name", "t_number"])
        # iterating over a pandas data frame is not an efficient way
        # check out vectorization
        for index, row in df.iterrows():
            self.add_student(row['first_name'], row['last_name'], row['t_number'])


class Course:
    def __init__(self, department, number, name, room, meeting_times):
        self.department = department
        self.number = number
        self.name = name
        self.room = room
        self.meeting_times = meeting_times


class CourseList:
    def __init__(self):
        self.course_list = []

    def add_course(self, department, number, name, room, meeting_times):
        self.course_list.append(Course(department, number, name, room, meeting_times))

    def find_course(self, department_to_find, number_to_find) -> int:
        for index, course in enumerate(self.course_list):
            if course.department == department_to_find and course.number == number_to_find:
                return index
        return -1

    def add_course_from_file(self, file_name):
        df = pd.read_csv(file_name, names=["department", "number", "name", "room", "meeting_times"])
        # iterating over a pandas data frame is not an efficient way
        # check out vectorization
        for index, row in df.iterrows():
            self.add_course(row["department"], row["number"], row["name"], row["room"], row["meeting_times"])


def main():
    course_list = CourseList()
    course_list.add_course_from_file('11.03 Courses.txt')

    student_list = StudentList()
    student_list.add_student_from_file('11.03 Students.txt')

    # pandas helps us to obtain data with ease from the .txt file
    df = pd.read_csv('11.03 Registration.txt', names=["t_number", "department", "number"])
    for index, row in df.iterrows():
        t_number, department, number = row['t_number'], row['department'], row['number']
        course_index = course_list.find_course(department, number)
        student_index = student_list.find_student(t_number)
        course = course_list.course_list[course_index]
        student_list.student_list[student_index].course_list.append(course)

    student_list.print_student_list()


if __name__ == '__main__':
    main()