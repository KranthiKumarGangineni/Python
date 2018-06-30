# Required Imports
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import ngrams, FreqDist

"""Reading from a File"""
with open('input.txt','r') as text_file:
    fileData = text_file.read()

# Word Tokenization - To get each Word from the Text
tokens = word_tokenize(fileData)

# Applying Lemmatization on the Words
lemmatizer = WordNetLemmatizer()
lemmatizerOutput = []
print("Lemmatized Output : \n")
for tok in tokens:
    # Iterating and Lemmatizing each word and Appending it to a list
    lemmatizerOutput.append(lemmatizer.lemmatize(str(tok)))
print(lemmatizerOutput)

# Applying BiGram using the Lemmatizer Output
print("Bigrams :\n")
bigramOutput = []
for big in ngrams(tokens, 2):
    # Fetching Bigrams using 'ngrams' method and Iterating it
    bigramOutput.append(big)
print(bigramOutput)

# BiGram- Word Frequency
# Using bigramOutput fetch the WordFreq Details
wordFreq = FreqDist(bigramOutput)
# Getting Most Common Words and Printing them - Will get the Counts from top to least
mostCommon = wordFreq.most_common()
print("BiGrams Frequency (From Top to Least) : \n", mostCommon)
# Fetching the Top 5 Bigrams
top5 = wordFreq.most_common(5)
print("Top 5 BiGrams : \n", top5)

# Going through Original Text
# Getting Sentences using Sentence Tokenization
sentTokens = sent_tokenize(fileData)
# Creating an Array to append the sentence
concatenatedArray = []
# Iterating the Sentences
for sentence in sentTokens:
    # Iterating the BiGrams present
    for a, b in bigramOutput:
        # Iterating the Top 5 BiGrams
        for ((c, m), length) in top5:
            # Comparing the each with each of the Top 5 Bigram
            if(a, b == c, m):
                concatenatedArray.append(sentence)

print("Concatenated Array : ",concatenatedArray)
print("Max of Concatenated Array : ", max(concatenatedArray))