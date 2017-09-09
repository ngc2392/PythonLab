#Write a pythin program that asks the user for five text strings.  The program
#should then report on whehter any of those strings is a sub-string of another (all such combinations
#should be reported)

stringOne = input("Enter the first string").lower();
stringTwo = input("Please enter the second string").lower();
stringThree = input("Please enter the third string").lower();
stringFour = input("Please enter the fourth string").lower();
stringFive = input("Please enter the fifth string").lower();

#only allow single words

if len(stringOne.split()) > 1:
    print("Your first string was more than one word")
    raise Exception("Please only enter one word")
elif len(stringTwo.split()) > 1:
    print("Your second string was more than one word")
    raise Exception("Please only enter one word")
elif len(stringThree.split()) > 1:
    print("Your third string was more than one word")
    raise Exception("Please only enter one word")
elif len(stringFour.split()) > 1:
    print("Your fourth string was more than one word")
    raise Exception("Please only enter one word")
elif len(stringFive.split()) > 1:
    print("Your fifth string was more than one word")
    raise Exception("Please only enter one word")
else:
    print("All strings entered are valid")


print(stringOne + " " + stringTwo + " " +  stringThree + " " + stringFour + " " + stringFive)

#put strings into a list
wordsList = [stringOne, stringTwo, stringThree, stringFour, stringFive];

for x in list(range(len(wordsList))):
    #print(wordsList[x])
    for y in list(range(len(wordsList))):
        if wordsList[x] in wordsList[y] and wordsList[x] is not wordsList[y]:
            #print("wordsList[x]: " + wordsList[x])
            #print("wordsList[y]: " + wordsList[y])
            print("'%s'" % wordsList[x] + " is a substring of " + wordsList[y])
        #else:
            #print("'%s'" % wordsList[x] + " is NOT a substring of " + wordsList[y])

#start at first string, check if that string is in the other ones

