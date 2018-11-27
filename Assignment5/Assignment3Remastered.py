#Write a new version of the program from Assignment 3.  Now you should
# read the input.txt from a file instead of from the user, and you should
# write your results to a new file.  Your program should begin by asking
# the user for the names of the input.txt and output files.  Handle punctuation
# in the spythonInput.txtame way as before.  Process all of the text in the file.



#get input.txt file
inputFile = input("Enter the input file")
outputFile = input("Enter the output file")

with open(inputFile, "r") as myFile:
    text = myFile.read().replace('\n', '')

print("Before lower case: " + text)

sentence = text.lower()

print("After lower case: " + text)

#remove puncation
sentence = sentence.replace(".", "")
sentence = sentence.replace(",", "")
sentence = sentence.replace(";", "")
sentence = sentence.replace(":", "")
sentence = sentence.replace("-", "")
sentence = sentence.replace("/", "")
sentence = sentence.replace("?", "")

print("Remove punctuation: " + sentence)

print("alphabetize words")

#put each word in a list
wordsList = sentence.split()

wordsList.sort()

finalText = ""

for word in wordsList:
    finalText = finalText + word + " "

writeFile = open(outputFile, "w")
writeFile.write(finalText)

















