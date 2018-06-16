import re
print("Program to validate password")

flag = 1
while flag == 1:
    password = input("Enter a password: ")
    # Checking for Length Validation
    if len(password)<6 or len(password)>16:
        print("Password must be 6 - 16 characters length")
        flag=1
    # Password is matched against Numbers Regular Expression
    elif re.search('[0-9]',password) is None:
        print("Password must have at least one number")
        flag = 1
    # Password should contain one of the special character
    elif re.search("[!@$*]", password) is None:
        print("Password  must have one special character [!$@*]")
        flag = 1
    # Password is matched against lowercase letters Regular Expression
    elif re.search('[a-z]',password) is None:
        print("Password must contain one Lower case Letter")
        flag = 1
    # Password is matched against uppercase letters Regular Expression
    elif re.search('[A-Z]',password) is None:
        print("Password must contain one Upper case Letter")
        flag = 1
    else:
        # If everything is fine, Come out of the Loop by setting flag as 0
        print("Entered password is OK")
        flag = 0