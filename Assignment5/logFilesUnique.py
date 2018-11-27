# Companies are often more interested in unique hits, that is,
# they want to know the number of distinct visitors that viewed
# a page.  Modify your previous script so that it only counts new
# views if the IP numbers are distinct.

from operator import itemgetter
from itertools import islice

dict = {}

#https://docs.python.org/3/library/functions.html#open
with open('logFiles.txt', 'rt') as f:
    for line in f:
        fileName = line.split()[0]
        ipAddress = line.split()[3]

        #key is file name
        key = fileName

        if key in dict:
                if ipAddress in dict[key]:
                    pass # we have seen this already
                else: # we haven't seen this ip yet
                    dict[key].append(ipAddress)
        else: # the page isn't in the dictionary yet
            dict[key] = []
            dict[key].append(ipAddress)

        print("The file name is " + fileName +".IP Address " + str(ipAddress) + "accessed it")

for key, value in dict.items():
    print(key, value)

print(' ')
print(' ')

# print top 10 pages in descending order
sortedDictionaryList = sorted(dict.items(), key=itemgetter(1), reverse=True)

iterator = islice(sortedDictionaryList, 10)

for item in iterator:
    fileName = item[0]
    fileHits = len(item[1])
    print("The file name is: " + fileName + " " + " with " + str(fileHits) + " unique hits")
    #print(item)

print(' ')
print(' ')


print("PRINTING DICTONARY")

dictionary = {}
iterator = islice(sortedDictionaryList, 10)
for item in iterator:
    fileName = item[0]
    fileHits = len(item[1])
    dictionary[fileName] = fileHits

for key, value in dictionary.items():
    print(key, value)

#output to logFilesResults.txt
sortedDictionaryList2 = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
iterator = islice(sortedDictionaryList2, 10)


for item in iterator:
    fileName = item[0]
    fileHits = item[1]

    print("The file name is: " + fileName + " " + " with " + str(fileHits) + " hits")

#output above console output to a file
iterator = islice(sortedDictionaryList2, 10)
with open('logFilesResultsUnique.txt', 'w') as output:
    output.write('File Name' + "                    " + " visits" + '\n')
    output.write('\n')
    output.write('\n')
    for item in iterator:
        fileName = item[0]
        fileHits = item[1]
        output.write(str(fileName) + " " + str(fileHits) + '\n')




