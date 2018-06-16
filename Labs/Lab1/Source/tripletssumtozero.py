values=input("Enter the list of numbers separated by space: ")
values= values.split(" ")
print("Given List:", values)


def findtriplets(array, n):
    count = 0;

    # Taking 3 for loops to match if any triples count becomes '0'
    # First, range from 0 to array length-2
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # Checking if the triplets sum is 0 or not
                if int(array[i]) + int(array[j]) + int(array[k]) == 0:
                    # Returning a Tuple if we find a Match that gives sum as 0
                    tup = (int(array[i]),int(array[j]),int(array[k]))
                    print("Matched Triplet that will give their sum as 0 : ", tup)
                    count = count+1

    if count == 0:
        print("No Such Triplet exist which will give sum as 0")


findtriplets(values,len(values))