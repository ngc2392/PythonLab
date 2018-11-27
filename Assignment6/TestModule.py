from DataFunctions import DataFunctionsModule as data

list = [17, 8, 3, 15, 78, 150, 92, 120]
smallestNumber = data.getMinimumEntry(list)
print("The smallest number is " + str(smallestNumber))


biggestNumber = data.getMaximumEntry(list)
print("The biggest number is " + str(biggestNumber))


kthEntry = 4
entry = data.kthLargestEntry(list, kthEntry)
print("The " + str(kthEntry) + "th " + "largest entry is " + str(entry))

median = data.getMedian(list)
print("The median is " + str(median))

list2 = [9, 2, 5, 4, 12, 7, 8, 11,9,3,7,4,12,5,4,10,9,6,9,4]
standardDeviation = data.getStandardDeviation(list2)
print("The standard deviation of the list is " + str(standardDeviation))