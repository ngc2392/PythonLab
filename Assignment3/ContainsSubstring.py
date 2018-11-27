#Write a python program that asks the user for five text strings.  The program
# should then report on whether any of those strings is a sub-string of another
# (all such combinations should be reported)

stringOne = input("Enter the first string").lower();
stringTwo = input("Please enter the second string").lower();
stringThree = input("Please enter the third string").lower();
stringFour = input("Please enter the fourth string").lower();
stringFive = input("Please enter the fifth string").lower();

print(stringOne + " " + stringTwo + " " + stringThree + " " + stringFour + " " + stringFive)

#put strings into a list
wordsList = [stringOne, stringTwo, stringThree, stringFour, stringFive];

for x in list(range(len(wordsList))):
    #print(wordsList[x])
    for y in list(range(len(wordsList))):
        if wordsList[x] in wordsList[y] and wordsList[x] is not wordsList[y]:
            print("'%s'" % wordsList[x] + " is a substring of " + wordsList[y])