print("program to find:\n1.Middle words\n2.Highest Length word\n3.Sentence in reverse order")

# Asking for User Input
sentence = input("Enter sentence:")

# Method Definition to find the Middle Word
def middle(sen):
    words=sen.split(" ")
    cenWord=[]
    # Finding the Center length
    center = int(len(words) / 2)

    # If length of words is an even number
    if len(words)%2 ==0 :
       # Getting the two values, as even numbers of sentences won't have a middle value
       cenWord.append(words[center-1])
       cenWord.append(words[center])
    else:
        # If Sentence length is Odd number, then we will be getting a single middle word
       cenWord=words[center]
    print("Middle words are:", cenWord)


def highestLength(sen):
    longWord=""
    words=sen.split(" ")
    for word in words:
        # Looping & checking the length of each word with other word and setting the maximum length word as longest one
        if(len(word)>len(longWord)):
            longWord=word
    print("Longest word is: ",longWord)


def reverse(sen):
    # Splitting the Words by space
    words=sen.split(" ")
    # Initializing a variable
    reverseSentence=""
    # Looping within the range of words
    for i in range(len(words)):
        for word in reversed(words[i]):
            # Looping the words using array indexing and adding the word to the sentence
            reverseSentence=reverseSentence+word
        reverseSentence=reverseSentence+" "
    print("Sentence with reverse words is: ", reverseSentence)


middle(sentence)
highestLength(sentence)
reverse(sentence)

