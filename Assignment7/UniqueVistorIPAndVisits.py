#Use a map to solve the following problem: write a function that accepts the name
#of a log file (formatted as in the the problem from Assignment 5).  This program
#should write a new file that shows the IP of each unique visitor (see the original
#problem for a discussion) and the number of distinct pages visited by that visitor.
#Use a dictionary indexed by the visitor IP to solve this problem

#get name of log file

logFileName = input("Enter the name of the log file")


def showIpOfUniqueVisitor(filename):

    logFileName = filename

    dictionary = {}

    with open(logFileName, 'rt') as f:
        for line in f:
            fileName = line.split()[0]
            ipAddress = line.split()[3]

            key = ipAddress

            if key in dictionary:
                if fileName in dictionary[key]:
                    pass
                else: # make the key
                    dictionary[key].append(fileName)
            else:
                dictionary[key] = []
                dictionary[key].append(fileName)

    writeToFile(dictionary)

    return dictionary


def writeToFile(tempDictonary):
    print("In writeToFile method")
    dictionary = tempDictonary

    with open("results.txt", 'w') as output:
        for key, value in dictionary.items():
            if(len(dictionary[key]) > 1):
                output.write(key + " visited " + str(len(dictionary[key])) + " distinct pages" + '\n')
            else:
                output.write(key + " visited " + str(len(dictionary[key])) + " distinct page" + '\n')

showIpOfUniqueVisitor(logFileName)