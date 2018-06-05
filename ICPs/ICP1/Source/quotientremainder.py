# ICP1

print('Program to get the Quotient and Remainder')

# Getting Inputs from the User
firstNumber = input('Please enter first number: ')
lastNumber = input('Please enter second number: ')

fn = int(firstNumber)
sn = int(lastNumber)

print('Below is output for getting quotient and remainder')
# n1 % n2 will get the Remainder
# n1//n2 will be (floored) quotient of n1 and n2
print("Remainder is : ", fn % sn, " & Quotient is : ", fn//sn)
