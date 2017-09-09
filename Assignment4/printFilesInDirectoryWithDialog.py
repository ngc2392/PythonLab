import os
import tkinter as tk
from tkinter import filedialog

def files_in_directory(path, extension):
    print(extension)
    arr_files = [x for x in os.listdir(path) if x.endswith("." + extension)]

    for x in range(len(arr_files)):
        print(arr_files[x])


#https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python

root = tk.Tk()
root.withdraw()

#file_path = filedialog.askopenfilename()
directory_path = filedialog.askdirectory()


files_in_directory(directory_path, "pdf")

