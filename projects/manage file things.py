from dataclasses import replace
import os
from os import walk
from os import listdir
from os.path import isfile, join


path = "/Users/lousergonne/Downloads/mathe_buch_2"
# path = "/Users/lousergonne/Downloads/"
extension = ""
lst = []

def rename_all_files_in_folder(folder_path, content, mode="None"):
    if mode == "None":
        print("no file extension")

        for (dirpath, dirnames, filenames) in walk(folder_path):
            content.extend(filenames)
        return content
    else:
        onlyfiles = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if 
        os.path.isfile(os.path.join(folder_path, f))]
        return onlyfiles
lst = rename_all_files_in_folder(path, lst, extension)

print(lst)
num1 = 0
while num1 <= len(lst):
    temp_path = lst[num1]
    new_path = str(temp_path).replace(".pdf", ".png")
    print("temporary path: ", temp_path)
    print("new path: ", new_path)
    os.rename(temp_path, new_path)
    num1 += 1