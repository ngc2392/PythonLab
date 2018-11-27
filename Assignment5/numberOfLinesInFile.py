# Write a program that counts the number of lines of text in a file and prints the answer on the console.
#This program takes its input from the file 'strings.txt'
num_lines = sum(1 for line in open("strings.txt"))
print(num_lines)