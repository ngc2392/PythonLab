#extend previous program

numberOfStrings = input("How many strings are you going to input")

numberOfStrings = int(numberOfStrings)

wordsList = [];
for i in range(numberOfStrings):
    #tempString = input("Please enter string " + i)
    tempString = input()
    wordsList.append(tempString)
    #print("'%s'" % wordsList[i] + " has been added")

for x in range(len(wordsList)):
    print("String number: " + str(x) + ":" + "" + wordsList[x])

for x in list(range(len(wordsList))):
    for y in list(range(len(wordsList))):
        if wordsList[x] in wordsList[y] and wordsList[x] is not wordsList[y]:
            print("'%s'" % wordsList[x] + " is a substring of " + wordsList[y])
