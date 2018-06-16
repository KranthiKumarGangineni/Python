def common(web, python):
    # Getting the Common people using intersection
    comm=set(web).intersection(python)
    # Using XOR operator, getting the Not Common People
    notcomm=list(set(web) ^ set(python))
    print("Common Students in both the classes:", comm)
    print("Not Common Students in both the classes:", notcomm)


webstudents = input("Please Enter List of Students Attending Web (Separated by a Comma):")
pythonStudents = input("Please Enter List of Students Attending Python (Separated by a Comma) :")

# Iterating the input by and forming a list
webstudents = [str(word) for word in webstudents.split(',')]
pythonStudents = [str(word) for word in pythonStudents.split(',')]
common(webstudents, pythonStudents)