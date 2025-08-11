from tkinter import *
from tkinter import filedialog, messagebox
import tkinter.font as tkFont

filename = None

root = Tk()

custom_font = tkFont.Font(family="Helvetica", size=20)

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!", message="Unable to save file...")

def openFile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root.title("My Python Text Editor")
root.minsize(width=800, height=800)
root.maxsize(width=800, height=800)

# Create a Text widget and store it in a variable
text = Text(root, font=custom_font)
text.pack(fill=BOTH, expand=True)

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()