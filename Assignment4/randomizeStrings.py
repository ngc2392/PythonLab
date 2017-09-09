#Use library facilities for random number generation
# to write a program that reads in a file and outputs
# a new file containing the same lines of text, but
# shuffled in a random order.  There are lots of ways to do this,
# some quite clever and short!  Read and explore.

#read file
#put each word into an array
#randomize the words
#put back into a string
#print string

import random


#https://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python
with open("strings.txt", "r") as myFile:
    data=myFile.read().replace('\n', '')



#https://stackoverflow.com/questions/2668312/shuffle-string-in-python
#https://stackoverflow.com/questions/22741319/what-does-random-sample-method-in-python-do

dataRandomized = ''.join(random.sample(data, len(data)))

print("from file: " + data)
print("randomzied: " + dataRandomized)

#write to the file
writeFile = open("randomizedStrings.txt", "w")
writeFile.write(dataRandomized)