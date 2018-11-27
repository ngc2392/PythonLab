# Write a program that reads a file that specifies how items are being processed.
# The file contains one word per line; for most lines, the word is the name of
# something that gets added to our stack.  In the special case of the word POP
# (all caps), we instead remove an item from the stack. Your program should simply process the file,
# and then print out the contents of the stack, in order from least- to most-recently added,
# after all the commands in the file have been processed.

list = []
with open('words.txt', 'rt') as r:
    for word in r:
        w = "".join(word.split()) # remove white space from word
        if w == "POP":
            list = list[:-1]
        else:
            list.append(w)

print("")
print("")

for x in list:
    print(x)
