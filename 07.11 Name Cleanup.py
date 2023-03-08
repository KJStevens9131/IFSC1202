#ProperCase(s)

#Returns a properly cases string s by uppercasing the first character and lowercasing the rest of the string.

#Hint: use upper() and lower() methods

def ProperCase(s):

    if len(s)==0:

        return ""

    elif len(s)==1:

        return s[0].upper()

        return s[0].upper()+s[1:].lower()

#RemoveCR(s)

#Returns a string with the carriage return ("\n") removed from string s

#Hint: use replace() method

def RemoveCR(s):

    return s.replace('\n', '')

#Trim(s)

#Returns a string with the leading and trailing spaces removed from string s.

#Hint: use strip() methoddef Trim(s):

def Trim(s):

    return s.strip()

#FirstName(s)

#Returns the first name of string s

#Hint: Find the first space in string s using the find() method

# Create a substring from the beginning of string s up to the first space

# Call the ProperCase function

def FirstName(s):

    ind = s.find(' ')

    return ProperCase(s[0:ind])

#LastName(s)

#Returns the last name of string s

#Hint: Find the last space in string s using the rfind() method

# Create a substring from the last space to the ending of sring s

# Call the ProperCase function

def LastName(s):

    ind = s.rfind(' ')

    return ProperCase(Trim(s[ind+1:]))

#MiddleName(s)

#Returns the middlename from string s

#Hint: Find the first space in string s using the find() method

# Find the last space in string s using the rfind() method

# Create a substing from the first space to the last space of string s

# Call the Trim function

# Call the ProperCase function

# If the length of the middle name is one, then it is an initial without a period. Append a period.

def MiddleName(s):

    firstInd = s.find(' ')

    lastInd = s.rfind(' ')

    st = s[firstInd:lastInd]

    st = Trim(st)

    st = ProperCase(st)

    if len(st)==1:

        st += '.'

    return st

# Print Headings

print("{:10s} {:10s} {:10s}".format("First","Middle","Last"))

print("{:10s} {:10s} {:10s}".format("-"*10,"-"*10,"-"*10))

# Open the names.txt file for reading

fp = open('07.11 Names.txt', 'r')

for line in fp.readlines():

    line = Trim(RemoveCR(line))

    fname = FirstName(line)

    lname = LastName(line)

    mname = MiddleName(line)

    print("{:10s} {:10s} {:10s}".format(fname,mname,lname))

fp.close()