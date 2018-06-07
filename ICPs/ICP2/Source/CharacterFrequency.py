# ICP2

# Asking for user input text file
fileName = input("What file do we need to get the character frequency? ")
# Opening and just reading the File
inFile = open(fileName,'r')
# Reads single line from the file
line = inFile.readline()

# Writing to a file
outFile = open("out.txt",'w')

while line != "":
    # Printing the Result
    print("%s,%d"%(line.rstrip("\n"), len(line.rstrip("\n"))))
    # Writing the result to Out file
    outFile.write("%s,%d\n"%(line.rstrip("\n"), len(line.rstrip("\n"))))
    # Reading the next line until it's empty
    line = inFile.readline()

# Closing the OutFile
outFile.close()
