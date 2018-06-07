# ICP2

print("Program to calculate the number of words in a string")

# ICP2

# Asking for user input text file
fileName = input("What file do we need to get number of words present? ")
# Opening and just reading the File
inFile = open(fileName,'r')
# Reads single line from the file
line = inFile.readline()

while line != "":
    length = 0
    # Here we are splitting the line based on the words and finding how many words in the line
    for str in line.split(" "):
        # Incrementing the Length each time a space is present in the line
        length += 1
    print("%s, %d" % (line.rstrip("\n"), length))

    # Reading the next line
    line = inFile.readline()