from sys import intern
import time
from tkinter.messagebox import YESNOCANCEL
from turtle import left
import numpy as np
import re
from time import time, strftime, localtime
from datetime import timedelta
from datetime import date
import os.path
import subprocess
import time
import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import *
from tkinter.ttk import *
import docx2txt
import pyautogui as pg
from PIL import Image

def run_internat(a):
    pass
def internat_automate(a, ba):
    pass
def internats_menu():
    pass
def log(aa):
    pass 

def automate(aa, ba):
    pass 

def run_menu(aa):
    pass 
menu_indesign_template  = 0
internat_indesign_template  = 0
# GUI

def overlay():
    root = tk.Tk()
    root.title('menu')
    root.geometry("1000x400")

    big_frame = ttk.Frame(root)
    big_frame.pack(fill="both", expand=True)

    source_check_lou = os.path.exists("/Users/lousergonne")
    source_check_NLNEW = os.path.exists("/Users/NLNEW")
 
    source_NLNEW = "/Users/NLNEW/Downloads/Sun-Valley-ttk-theme-master/sun-valley.tcl"
    source_lou = "/Users/lousergonne/Documents/Sun-Valley-ttk-theme-master/sun-valley.tcl"
   
    if source_check_lou == True:
        source = source_lou
    elif source_check_NLNEW:
        source = source_NLNEW
   
    
    root.tk.call("source", source)
    root.tk.call("set_theme", "dark")

    def change_theme():
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            root.tk.call("set_theme", "light")
        else:
            root.tk.call("set_theme", "dark")

    # Remember, you have to use ttk widgets

    def open_file():

        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a txt file",
                                                   filetypes=filetypes)

        ttk.Label(big_frame, text="origin file: " + root.filename).pack(pady=10)

        file_name = root.filename
        ttk.Label(big_frame, text="processing...").pack()
        start = time.time()
        log("Start Program")
        
        print("file name: ", file_name)
        print()
        menu_data = file(file_name)
        xml_file_name = run_menu(menu_data)
        automate(menu_indesign_template, xml_file_name)

        ttk.Label(big_frame, text="menu number: " + xml_file_name).pack(pady=10, padx=10)

        end = time.time()
        elapsed_time = end-start
        elapsed_time = round(elapsed_time, 2)
        ttk.Label(big_frame, text=f"runtime: {elapsed_time}").pack(pady=10, padx=10)

        log("done")
    def internat_open_file():

        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a txt file",
                                                   filetypes=filetypes)

        ttk.Label(big_frame, text="origin file: " + root.filename).pack(pady=10)

        file_name = root.filename
        ttk.Label(big_frame, text="processing...").pack()
        start = time.time()
        log("Start Program")
        
        print("file name: ", file_name)
        print()
        menu_data = file(file_name)
        xml_file_name = internats_menu(menu_data)

        # automate(indesign_template, xml_file_name)
        # after thisss

        ttk.Label(big_frame, text="internats menu number: " + xml_file_name).pack(pady=10, padx=10)

        end = time.time()
        elapsed_time = end-start
        elapsed_time = round(elapsed_time, 2)
        ttk.Label(big_frame, text=f"runtime: {elapsed_time}").pack(pady=10, padx=10)

        log("done")

    def file(file_name):
        if ".txt" in file_name:
            f = open(f"{file_name}", "r")
            file_txt = f.read()
        elif ".docx" in file_name:
            file_txt = docx2txt.process(file_name)
        else:
            ttk.Label(big_frame, text="file not compatible").pack(pady=10, padx=10, side="left")
            raise ValueError("file not compatible")
        return file_txt

    menu_file_select = ttk.Label(big_frame, text="select your menu file")
    menu_file_select.pack(pady=10)
    menu_filebutton = ttk.Button(big_frame, text="open file", command=open_file)
    menu_filebutton.pack(pady=10)

    internat_file_select = ttk.Label(big_frame, text="select your internat file")
    internat_file_select.pack(pady=10)
    internat_filebutton = ttk.Button(big_frame, text="open file", command=internat_open_file)
    internat_filebutton.pack(pady=10)

    button = ttk.Button(root, text="Change theme!", command=change_theme)
    button.pack(pady=10)
    
    root.mainloop()
    


def overlay2():

    menu_col = 2
    internat_col = 4
    root = tk.Tk()
    root.title('menu')
    root.geometry("1000x400")


    source_check_lou = os.path.exists("/Users/lousergonne")
    source_check_NLNEW = os.path.exists("/Users/NLNEW")
 
    source_NLNEW = "/Users/NLNEW/Downloads/Sun-Valley-ttk-theme-master/sun-valley.tcl"
    source_lou = "/Users/lousergonne/Documents/Sun-Valley-ttk-theme-master/sun-valley.tcl"
   
    if source_check_lou == True:
        source = source_lou
    elif source_check_NLNEW:
        source = source_NLNEW
   
    
    root.tk.call("source", source)
    root.tk.call("set_theme", "dark")

    def change_theme():
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            root.tk.call("set_theme", "light")
        else:
            root.tk.call("set_theme", "dark")

    # Remember, you have to use ttk widgets

    def open_file():

        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a txt file",
                                                   filetypes=filetypes)
        ttk.Label(root).grid(row=5, column=menu_col)

        ttk.Label(root, text="origin file: " + root.filename).grid(row=6, column=menu_col)
        ttk.Label(root).grid(row=7, column=menu_col)

        file_name = root.filename
        ttk.Label(root, text="processing...").grid(row=8, column=menu_col)
        start = time.time()
        log("Start Program")
        
        print("file name: ", file_name)
        print()
        menu_data = file(file_name)
        xml_file_name = run_menu(menu_data)
        automate(menu_indesign_template, xml_file_name)
        ttk.Label(root).grid(row=9, column=menu_col)

        ttk.Label(root, text="menu number: " + xml_file_name).grid(row=10, column=menu_col)
        ttk.Label(root).grid(row=11, column=menu_col)

        end = time.time()
        elapsed_time = end-start
        elapsed_time = round(elapsed_time, menu_col)
        ttk.Label(root, text=f"runtime: {elapsed_time}").grid(row=12, column=menu_col)

        log("done")

    def internat_open_file():

        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a txt file",
                                                   filetypes=filetypes)

        ttk.Label(root, text="origin file: " + root.filename).grid(row=5,  column=internat_col)

        file_name = root.filename
        ttk.Label(root, text="processing...").grid(row=6, column=internat_col)
        start = time.time()
        log("Start Program")
        
        print("file name: ", file_name)
        print()
        menu_data = internat_file(file_name)
        xml_file_name = internats_menu(menu_data)

        # automate(indesign_template, xml_file_name)
        # after thisss

        ttk.Label(root, text="internats menu number: " + xml_file_name).grid(row=7, column=internat_col)

        end = time.time()
        elapsed_time = end-start
        elapsed_time = round(elapsed_time, 2)
        ttk.Label(root, text=f"runtime: {elapsed_time}").grid(row=8, column=internat_col)

        log("done")

    def file(file_name):
        if ".txt" in file_name:
            f = open(f"{file_name}", "r")
            file_txt = f.read()
        elif ".docx" in file_name:
            file_txt = docx2txt.process(file_name)
        else:
            ttk.Label(root, text="file not compatible").grid(row=9, column=menu_col)
            raise ValueError("file not compatible")
        return file_txt

    def internat_file(file_name):
        if ".txt" in file_name:
            f = open(f"{file_name}", "r")
            file_txt = f.read()
        elif ".docx" in file_name:
            file_txt = docx2txt.process(file_name)
        else:
            ttk.Label(root, text="file not compatible").grid(row=9, column=internat_col)
            raise ValueError("file not compatible")
        return file_txt
    
    ttk.Label(root).grid(row=2, column=1)
    ttk.Label(root).grid(row=2, column=3)
    ttk.Label(root).grid(row=2, column=4)
    ttk.Label(root, ).grid(row=3, column=5)

    txt = 11
    w = ttk.Label(root, text=txt)
    w.grid(row=1, column=menu_col)

    menu_file_select = ttk.Label(root, text="select your menu file")
    menu_file_select.grid(row=4, column=menu_col)

    menu_filebutton = ttk.Button(root, text="open file", command=open_file)
    menu_filebutton.grid(row=6, column=menu_col)

    w = ttk.Label(root, text=txt)
    w.grid(row=2, column=menu_col)


    w = ttk.Label(root, text=txt)
    w.grid(row=1, column=menu_col)

    w = ttk.Label(root, text=txt)
    w.grid(row=1, column=internat_col)


    internat_file_select = ttk.Label(root, text="select your internat file")
    internat_file_select.grid(row=4, column=internat_col)

    w = ttk.Label(root, text=txt)
    w.grid(row=3, column=internat_col)

    internat_filebutton = ttk.Button(root, text="open file", command=internat_open_file)
    internat_filebutton.grid(row=6, column=internat_col)

    button = ttk.Button(root, text="Change theme!", command=change_theme)
    button.grid(row=10, column=8)
    
    root.mainloop()

def internat_open_file(cord_x, cord_y, root):
    pass

def overlay():
    root = tk.Tk()
    root.title('menu')
    root.geometry("1000x300")

    menu_col = 2
    internat_col = 4
    source_check_lou = os.path.exists("/Users/lousergonne")
    source_check_NLNEW = os.path.exists("/Users/NLNEW")
 
    source_NLNEW = "/Users/NLNEW/Downloads/Sun-Valley-ttk-theme-master/sun-valley.tcl"
    source_lou = "/Users/lousergonne/Documents/Sun-Valley-ttk-theme-master/sun-valley.tcl"
   
    if source_check_lou == True:
        source = source_lou
    elif source_check_NLNEW:
        source = source_NLNEW
   
    
    root.tk.call("source", source)
    root.tk.call("set_theme", "dark")

    def change_theme():
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            root.tk.call("set_theme", "light")
        else:
            root.tk.call("set_theme", "dark")

    def file(file_name):
        if ".txt" in file_name:
            f = open(f"{file_name}", "r")
            file_txt = f.read()
        elif ".docx" in file_name:
            file_txt = docx2txt.process(file_name)
        else:
            ttk.Label(root, text="file not compatible").grid(row=9, column=menu_col)
            raise ValueError("file not compatible")
        return file_txt

    def internat_file(file_name):
        if ".txt" in file_name:
            f = open(f"{file_name}", "r")
            file_txt = f.read()
        elif ".docx" in file_name:
            file_txt = docx2txt.process(file_name)
        else:
            ttk.Label(root, text="file not compatible").grid(row=9, column=internat_col)
            raise ValueError("file not compatible")
        return file_txt
    
    def run_men():
        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a file",
                                                   filetypes=filetypes)
        w = ttk.Label(root, text=f"file: {root.filename}")

        w.grid(row=6, column=menu_col)
        start = time.time()
        originfile_name = root.filename
        menu_contents = file(originfile_name)
        menu_filename = run_menu(menu_contents)
        automate(menu_indesign_template, menu_filename)

        ttk.Label(root, text=f"menu number: {menu_filename}").grid(row=8, column=menu_col)

        end = time.time()
        elapsed_time = end-start
        elapsed_time = round(elapsed_time, menu_col)
        ttk.Label(root, text=f"runtime: {elapsed_time}").grid(row=10, column=menu_col)

        log("done")

    

    def run_inter():
        filetypes = (
            ('All files', '*.*'),
            ('word files', '*.docx'),
            ('text files', '*.txt'),
            ('rich text files', '*.rtf')
        )

        root.filename = filedialog.askopenfilename(initialdir="/Volumes/Desktop", title="select a file",
                                                   filetypes=filetypes)

        w = ttk.Label(root, text=f"file: {root.filename}")
        w.grid(row=6, column=internat_col)

        start = time.time()
        originfile_name = root.filename
        internat_contents = internat_file(originfile_name)
        internat_filename = run_internat(internat_contents)
        automate(internat_indesign_template, internat_filename)

        ttk.Label(root, text=f"internat number: {internat_filename}").grid(row=8, column=internat_col)

        end = time.time()
        elapsed_time = end-start
        elapsed_time = round(elapsed_time, menu_col)
        ttk.Label(root, text=f"runtime: {elapsed_time}").grid(row=10, column=internat_col)

        log("done")

    
    w = ttk.Label(root, text="⠀").grid(row=1, column=1, padx=10)
    w = ttk.Label(root, text="⠀").grid(row=2, column=2,)
    w = ttk.Label(root, text="⠀").grid(row=3, column=3,)
    w = ttk.Label(root, text="⠀").grid(row=4, column=4,)
    w = ttk.Label(root, text="⠀").grid(row=5, column=5,)
    w = ttk.Label(root, text="⠀").grid(row=6, column=6,)
    w = ttk.Label(root, text="⠀").grid(row=7, column=7,)
    w = ttk.Label(root, text="⠀").grid(row=8, column=8,)
    w = ttk.Label(root, text="⠀").grid(row=9, column=9,)
    w = ttk.Label(root, text="⠀").grid(row=10, column=10,)
    w = ttk.Label(root, text="⠀").grid(row=11, column=11,)
    w = ttk.Label(root, text="⠀").grid(row=12, column=12,)
    w = ttk.Label(root, text="⠀").grid(row=13, column=13)
    w = ttk.Label(root, text="⠀").grid(row=14, column=14,)
    w = ttk.Label(root, text="⠀").grid(row=15, column=15)
    w = ttk.Label(root, text="⠀").grid(row=16, column=16)

    menu_txt = ttk.Label(root, text="open you menu file")
    menu_txt.grid(row=2, column=menu_col)
    
    menu_filebutton = ttk.Button(root, text="open file", command=run_men)
    menu_filebutton.grid(row=4, column=menu_col)
    

    internat_txt = ttk.Label(root, text="open your internat file")
    internat_txt.grid(row=2, column=internat_col)

    internat_filebutton = ttk.Button(root, text="open file", command=run_inter)
    internat_filebutton.grid(row=4, column=internat_col)

    button = ttk.Button(root, text="Change theme!", command=change_theme)
    button.grid(row=16, column=3)

    root.mainloop()
overlay()