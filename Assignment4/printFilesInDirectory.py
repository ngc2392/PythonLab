# printFileInDirectoryWithDialog.py does the same thing, but with a dialog box

import os

#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

def files_in_directory(path, extension):
    print(extension)
    arr_files = [x for x in os.listdir(path) if x.endswith("."+extension)]
    return arr_files

#prints everything in directory, regardless of extension
def everything_in_directory(path):
    arr_files = [x for x in os.listdir(path)]
    return arr_files

files = files_in_directory("/Users/LoganPhillips/Desktop", "iso")

for x in range(len(files)):
    print(files[x])

#files = everything_in_directory("/Users/LoganPhillips/Desktop")

#for x in range(len(files)):
    #print(files[x])