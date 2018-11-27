#Analyzing data module

from math import sqrt

def getMinimumEntry(list_of_numbers):
    tempList = list_of_numbers

    minValue = tempList[0]
    for x in tempList:
        if x < minValue:
            minValue = x
    return minValue

def getMaximumEntry(list_of_numbers):
    tempList = list_of_numbers

    maxValue = tempList[0]
    for x in tempList:
        if x > maxValue:
            maxValue = x
    return maxValue

def kthLargestEntry(list_of_numbers, k):
    tempList = list_of_numbers

    sortedList = sorted(tempList) # sort in ascending order

    entry = sortedList[k]

    for x in sortedList:
        print(x)

    return entry

def getMedian(list_of_numbers):
    tempList = list_of_numbers
    tempList.sort()
    median = 0
    lengthOfList = len(tempList)
    if lengthOfList % 2 != 0:
        middle = (lengthOfList/2)
        median = tempList[int(middle)]
    else:
        firstNum = (lengthOfList / 2) - 1
        secondNum = (lengthOfList / 2)
        median = float(tempList[int(firstNum)] + tempList[int(secondNum)]) / float(2)
    return median

#standard deviation is a measure of how spread out numbers are

# Work out the Mean
#For each number, subtract the Mean
    #Square the result
#Work out the mean of those squared differences
#Take the square root of that

#https://www.mathsisfun.com/data/standard-deviation-formulas.html
def getStandardDeviation(list_of_numbers):
    tempList = list_of_numbers

    #work out the mean
    total = 0
    for x in tempList:
        total = total + x

    mean = total / len(tempList)


    squaredDifferences = []

    #for each number, subtract the mean, square the result
    for x in tempList:
        tempDifference = x - mean
        tempSquaredDifference = tempDifference * tempDifference
        squaredDifferences.append(tempSquaredDifference)

    #work out the mean for those squared differences
    total2 = 0
    for x in squaredDifferences:
        total2 = total2 + x
    squaredDifferenceMean = total2 / len(squaredDifferences)

    #take the square root
    sd = sqrt(squaredDifferenceMean)

    return sd


