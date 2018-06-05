# ICP1

print('Program to Reverse the Name')

# Getting Inputs from the User
firstName = input('Please enter your first name: ')
lastName = input('Please enter your last name: ')

fn = str(firstName)
ln = str(lastName)

# Concatenating the name
fullName = fn+" "+ln

print('Below is output for reverse naming')
# Printing the Name in reverse order - Extended Slice Syntax
# Ref: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
print(fullName[::-1])
