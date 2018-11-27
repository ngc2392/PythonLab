#Extend the previous program to lift the restriction to five strings;
# first ask the user how many strings she will enter, then read in and analyze all of them

numberOfStrings = input("How many strings are you going to input.txt")

numberOfStrings = int(numberOfStrings)

wordsList = [];
for i in range(numberOfStrings):
    tempString = input()
    wordsList.append(tempString)

for x in range(len(wordsList)):
    print("String number: " + str(x) + ":" + "" + wordsList[x])

for x in list(range(len(wordsList))):
    for y in list(range(len(wordsList))):
        if wordsList[x] in wordsList[y] and wordsList[x] is not wordsList[y]:
            print("'%s'" % wordsList[x] + " is a substring of " + wordsList[y])
