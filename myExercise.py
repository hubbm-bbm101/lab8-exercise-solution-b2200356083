import sys

with open(sys.argv[1], "r") as file:
    students = file.readlines()    
    d = {}
    names = sys.argv[2].split(",")
    for student in students:
        student = student.split(":")
        d[student[0]]= student[1]
    for ourStudent in names:
        try:
            print("Name: {}, University: {}".format(ourStudent,d[ourStudent]), end="")   
        except: 
            print("No record of '{}' was found".format(ourStudent))

