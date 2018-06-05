import random

print('Program to check if random number is matching with the user input number')

numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Getting a Random Number
randomNum = random.choice(numList)
print("Random Number: ", randomNum)

# Setting a Flag first which will be used in while loop
flag = 1


while flag == 1:
    # Asks for the input first ( and also again and again until the input number is matching with random number)
    inputNumber = int(input('Please enter your number: '))
    if inputNumber >= randomNum:
        if inputNumber == randomNum:
                                print("You have guessed it correct !!")
                                # Breaking the loop and exiting once numbers are matched
                                break
        else:
            print("Your number is greater than the random number")
            # With below condition, user input is asked again
            flag = 1
    else:
        print("Your number is lesser than the random number")
        # With below condition, user input is asked again
        flag = 1


