#Write a program that reads in a sentence and outputs the words
# in that sentence, all lowercase and ordered alphabetically
import string
import re

#read in a sentence
sentence = input("Please enter a sentence")

#put sentence to lowercase
sentence = sentence.lower()
print("To lower case " + sentence)

#https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate

#remove puncutation
print(string.punctuation)
#sentence = sentence.strip(string.punctuation)
translator = str.maketrans('','', string.punctuation)
sentence = sentence.translate((translator))
print("Remove punctuation: " + sentence)

print("alphabetize words")

#put each word in a list
wordsList = re.sub("[^\w]", " ", sentence).split()

for word in wordsList:
    print(word)

wordsList.sort()

finalSentence = ""

for word in wordsList:
    finalSentence = finalSentence + word + " "

print(finalSentence)