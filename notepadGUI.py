""" notepad but GUI v2"""
import datetime
import os
import platform
import tkinter
import shelve
from tkinter import filedialog
from tkinter import messagebox

print(f"Program started at {datetime.datetime.now()}")
root = tkinter.Tk()
root.configure(background="Black")
root.title("Notepad GUI v2.0")

if platform.system() == "Windows":
    initialPath = os.getenv("USERPROFILE")
    if not os.access(f"{initialPath}/Documents/update", os.F_OK):
        os.mkdir(f"{initialPath}/Documents/update")
    with shelve.open(f"{initialPath}/Documents/update/updater") as updatePath:
        updatePath["filepath"] = os.getcwd()
        updatePath["fullpath"] = f"{updatePath['filepath']}/notepadGUI.py"
else:
    initialPath = os.getenv("HOME")


def updater(event=None):
    """ update program"""
    update.destroy()
    wannaUpdate.destroy()
    os.chdir("/")
    os.system(f"python {initialPath}/Documents/updater.py")
    os.remove(f"{initialPath}/Documents/updater.py")


def addBrace(event=None):
    """ add left curly brace automatically"""
    print("called addBrace() function")
    indexer = text.index(tkinter.INSERT)
    text.insert(indexer, "}")


def addSquareBracket(event=None):
    """ add left square bracket (used for list) automatically"""
    print("called addSquareBracket() function")
    indexer = text.index(tkinter.INSERT)
    text.insert(indexer, "]")


def addBracket(event=None):
    """ add left parenthesis automatically"""
    print("called addBracket() function")
    indexer = text.index(tkinter.INSERT)
    text.insert(indexer, ")")


def save(event=None):
    """save files"""
    print("called save() function")
    try:
        with open(saveTo.get(1.0, tkinter.END).removesuffix("\n"), "w") as\
                writer:
            writer.write(text.get(1.0, tkinter.END))
        saveButton.config(text="Saved file")
        root.title(f"{saveTo.get(1.0, tkinter.END)} - Notepad")
    except FileNotFoundError:

        def folderCreate():
            """ create folder if it doesn't exist!"""
            os.mkdir(createFolderText.get(1.0, tkinter.END).removesuffix("\n"))

        createFolder = tkinter.Tk()
        msg = tkinter.Label(createFolder, text="Create the folder before "
                                               "saving a file in that folder!")
        msg.grid(row=0, column=0, columnspan=2)
        createFolderText = tkinter.Text(createFolder, width=40, height=2)
        createFolderText.grid(row=1, column=0, padx=30, pady=30)
        createFolderButton = tkinter.Button(createFolder, text="Create folder!",
                                            command=folderCreate)
        createFolderButton.grid(row=2, column=0)
        createFolder.mainloop()


def readFile(event=None):
    """ read files"""
    print("called readFile() function")
    root.title("Notepad GUI v2.0")
    filetype = (
        ("Text documents (.txt)", "*.txt"),
        ("HTML Files (.html and .htm)", "*.html" and "*.htm"),
        ("Python files (.py)", ".py"),
        ("C++ files (.cpp)", "*.cpp"),
        ("JS Files (.js)", "*.js"),
        ("All types (*)", "*.*"),
    )
    filePath = filedialog.askopenfilename(title="Open file to read",
                                          filetypes=filetype)
    print(filePath)
    try:
        with open(filePath, "r") as reader:
            returnReader = reader.read()
        saveTo.delete(1.0, tkinter.END)
        text.delete(1.0, tkinter.END)
        text.insert(1.0, returnReader)
        saveTo.insert(1.0, filePath)
        root.title(f"{filePath} - Notepad")
    except FileNotFoundError:
        messagebox.showerror("File not found!", "The selected file doesn't "
                                                "exist! so, we can't open it. "
                                                "reverted changes")


def deleter(event=None):
    """ delete files"""
    print("called deleter() function")
    if os.access(saveTo.get(1.0, tkinter.END).removesuffix("\n"), os.F_OK):
        os.remove(saveTo.get(1.0, tkinter.END).removesuffix("\n"))
        text.delete(1.0, tkinter.END)
        saveTo.delete(1.0, tkinter.END)
        root.title("Notepad GUI v2.0")
    else:
        messagebox.showerror("File doesn't exist", "The file you are trying "
                                                   "to delete doesn't exist!")


def clear(event=None):
    """ clear text """
    print("called clear() function")
    text.delete(1.0, tkinter.END)


def programmerMode(event=None):
    """ enables programmer mode, automatic parenthesis completion"""
    print("called programmerMode() function")
    root.bind("<(>", addBracket)
    root.bind("<{>", addBrace)
    root.bind("<[>", addSquareBracket)
    programMode.configure(text="Disable Programmer Mode",
                          command=disableProgrammerMode)


def disableProgrammerMode(event=None):
    """ disable programmer mode"""
    print("called disableProgrammerMode() function")
    root.unbind("<(>")
    root.unbind("<{>")
    root.unbind("<[>")
    programMode.configure(text="Enable Programmer Mode",
                          command=programmerMode)


text = tkinter.Text(root, height=20, width=100, font=("Arial Rounded MT Bold",
                                                      18))
text.grid(row=0, column=0, pady=10)
saveTo = tkinter.Text(root, height=2, width=50, font=("Arial Rounded MT Bold",
                                                      12))
saveTo.grid(row=1, column=0)
buttonFrame = tkinter.Frame(root, background="Black", pady=10)
buttonFrame.grid(row=2, column=0)
saveTo.insert(1.0, f"{initialPath}/Documents/notes.txt")
print(f"Set initial path to {initialPath}/Documents/notes.txt")
print("Initialized button frame")
saveButton = tkinter.Button(buttonFrame, text="Save file", command=save)
saveButton.grid(row=0, column=0)
readButton = tkinter.Button(buttonFrame, text="Read file", command=readFile)
readButton.grid(row=0, column=1, padx=20)
deleteButton = tkinter.Button(buttonFrame, text="Delete file", command=deleter)
deleteButton.grid(row=0, column=2)
clearText = tkinter.Button(buttonFrame, text="Clear text", command=clear)
clearText.grid(row=0, column=3, padx=20)
programMode = tkinter.Button(buttonFrame, text="Enable Programmer mode",
                             command=programmerMode)
programMode.grid(row=0, column=4)
print("Initialized the buttons to get into buttonFrame")
root.bind("<Control-r>", readFile)
root.bind("<Control-s>", save)
root.bind("<Control-d>", deleter)
root.bind("<Control-l>", clear)
root.bind("<Control-p>", programmerMode)
root.bind("<Control-P>", disableProgrammerMode)
print("Bound keyboard shortcuts")
if os.access(f"{initialPath}/Documents/updater.py", os.F_OK):
    update = tkinter.Label(root, text="Update is available! install now!")
    update.grid(row=3, column=0)
    wannaUpdate = tkinter.Button(buttonFrame, text="Update", command=updater)
    wannaUpdate.grid(row=0, column=5, padx=20)
    root.bind("<Alt-d>", updater)
root.mainloop()
print(f"Exited the program at {datetime.datetime.now()} ! adding an input so "
      f"that from py.exe the console will still be up there showing logs!")
input()
