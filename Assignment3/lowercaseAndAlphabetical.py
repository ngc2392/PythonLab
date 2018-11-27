#Write a program that reads in a sentence and outputs the words
# in that sentence, all lowercase and ordered alphabetically

# read in a sentence
sentence = input("Please enter a sentence")

# put sentence to lowercase
sentence = sentence.lower()
print("To lower case " + sentence)

#https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate

#remove punctuation

sentence = sentence.replace(".", "")
sentence = sentence.replace(",", "")
sentence = sentence.replace(";", "")
sentence = sentence.replace(":", "")
sentence = sentence.replace("-", "")
sentence = sentence.replace("/", "")
sentence = sentence.replace("?", "")

print("AFTER REMOVAL: " + " " + sentence)

#put each word in a list
wordsList = sentence.split()

print("alphabetize words")
wordsList.sort()

finalSentence = ""

for word in wordsList:
    finalSentence = finalSentence + word + " "

print(finalSentence)

