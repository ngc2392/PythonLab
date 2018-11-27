import random

lines = open('strings.txt').readlines()
random.shuffle(lines)
writeFile = open("randomizedStrings.txt", "w")
for x in range(0,len(lines)):
    writeFile.write(lines[x] + "\n")