import tkinter
from tkinterdnd2 import *

def drop(event):
    entry_sv.set(event.data)
    print(entry_sv,
    event.data,
    event)

root = TkinterDnD.Tk()
entry_sv = tkinter.StringVar()
entry = tkinter.Entry(root, textvar=entry_sv, width=80)
entry.pack(fill=tkinter.X)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)
print(entry_sv,
entry)
root.mainloop()