# Returns a properly cased string s y uppercasing the First
# character and lowercasing the rest of the string
def ProperCase(s):
# uppercasing fist letter and other in lowercase
    return s[0].upper()+s[1:].lower()

# Returns a string with the carraige return ("\n") removed from string s
def RemoveCR(s):
# replacing all "\n" with empty string
    s.replace("\n",'')
    return s

# Returns a string with the leading and trailing spaces removed from
# string s
def Trim(s):
    return s.strip()

# Returns the first name of string s
def FirstName(s):
    index = s.find(' ') # find first index of any space
    substring = s[:index] #creating a substring upto that space.
    return ProperCase(substring) #returning substring with Proper Case.

# Returns the last name of string s
def LastName(s):
    index = s.rfind(' ') #find the last space in string s.
    substring = s[index+1:] # creating a substring from last space to the end.
    return ProperCase(substring) #return substring with Proper Case

# Returns the middle name from string s
def MiddleName(s):
    index1 = s.find(' ') #find the first space in string s.
    index2 = s.rfind(' ') #find the last space in string s.
    if index1 == index2: # if both index are same means no MiddleName
        return '' # return empty string
# if both index are not same
    s1 = Trim(s[index1:index2]) #create a substring and remove any extra spaces
    s1 = ProperCase(s1) # properly cases the string s using ProperCase()
    if(len(s1)==1): #if length of the middleName is 1 means it is a initial
        s1=s1+'.' #append a period at the end
    return s1 #return middleName

#read filename from user as input
filename = input("Enter file name: ")
filename = filename+'.txt' #append .txt to filename
# printing heading
print("{:10s} {:10s} {:10s}".format("First","Middle","Last"))
print("{:10s} {:10s} {:10s}".format("-"*10,"-"*10,"-"*10))
# open the names.txt file for reading
with open(filename) as f:
#read whole file at once line by line and returns a list of all lines
    lines = f.readlines()
    for line in lines: #for each line in lines list
        line = Trim(line) #removes leading and trailing spaces
        line = RemoveCR(line) #removes carraige return ("\n") from line
    if line!='': #if line is not empty an empty string
        fn = FirstName(line) #get FirstName from line
        ln = LastName(line) # get LastName from line
        mn = MiddleName(line) #get MiddleName from line
# printing FirstName,MiddleName and LastName sequentially
    print("{:10s} {:10s} {:10s}".format(fn,mn,ln))