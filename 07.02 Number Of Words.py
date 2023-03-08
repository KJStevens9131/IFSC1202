def check_space(string):
     
    
    count = 0
     
    for i in range(0, len(string)):
         
       
        if string[i] == " ":
            count += 1
         
    return count
 

string = input("Enter your sentence: ")
 

print("number of words",check_space(string)+1)