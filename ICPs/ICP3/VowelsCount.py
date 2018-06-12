# ICP3
print('Program to return the Count of the Vowels')

# Vowels set
vowels = {'a', 'e', 'i', 'o', 'u'}

# Getting Input from the User
sentence = input('Please enter your sentence to get vowels count: ')

# Counters
noDuplicateCount = 0
withDuplicateCount = 0

# Dictionary
dictionary = {}

# Iterating each word in the given sentence
for word in sentence:
    # Checking if the word is a part of vowels set
    if word in vowels:
        # No Duplicate of Vowels Case
        ''' If the word is not present in dictionary, then adding it to dictionary and increasing the counter
        This, will make sure we get correct vowel count even if duplicates are present. '''
        if word not in dictionary:
            dictionary[word] = 1
            noDuplicateCount = noDuplicateCount + 1
        # Considering with Duplicates
        withDuplicateCount = withDuplicateCount+1

print("Vowels count (Considering Duplicates) --> ", noDuplicateCount)
print("Vowels count (Not Considering Duplicate Vowels) --> ", withDuplicateCount)

