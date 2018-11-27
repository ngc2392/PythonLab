#first entry is the page that was accessed
#second entry is teh date
#third entry is the time
#fourth entry is the IP address of the computer that requested the page
from operator import itemgetter
from itertools import islice


lines = []
with open ('logFiles.txt', 'rt') as f:
    for line in f:
        lines.append(line)
print(lines[1])
# go through each line and get the name

# parition only splits the string at the first occurrence of teh given argument,
# split splits the string at any occurence of the given argument

dict = {}

for x in lines:
    tempFileName = x.partition(' ')[0]
    print("The file name is " + tempFileName)
    key = tempFileName
    if key in dict:
        hits = dict[tempFileName]
        dict[tempFileName] = hits + 1
    else: #add the file as a key
        dict[tempFileName] = 1

print(' ')
print(' ')

#print out the keys and values
for key, value in dict.items():
    print(key, value)

print(' ')
print(' ')

# print top 10 pages in descending order
sortedDictionaryList = sorted(dict.items(), key=itemgetter(1), reverse=True)

iterator = islice(sortedDictionaryList, 10)
for item in iterator:
    fileName = item[0]
    fileHits = item[1]

    print("The file name is: " + fileName + " " + " with " + str(fileHits) + " hits")


#output to logFilesResults.txt
sortedDictionaryList = sorted(dict.items(), key=itemgetter(1), reverse=True)

iterator = islice(sortedDictionaryList, 10)

with open('logFilesResults.txt', 'w') as output:
    output.write('File Name' + "                    " + " visits" + '\n')
    output.write('\n')
    output.write('\n')
    for item in iterator:
        fileName = item[0]
        fileHits = item[1]
        output.write(str(fileName) + " " + str(fileHits) + '\n')
