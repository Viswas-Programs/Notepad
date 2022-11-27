import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.configure(background="Black")


def save(event=None):
    with open(saveTo.get(1.0, tkinter.END), "a") as writer:
        writer.write(text.get(1.0, tkinter.END))
    saveButton.config(text="Saved file")


def readFile(event=None):
    filetype = (
        ("Text documents (.txt)", "*.txt"),
        ("All types (*)", "*.*")
    )
    filePath = filedialog.askopenfile(title="Open file to read", filetypes=filetype)
    with open(filePath, "a") as writer:
        reader = writer.read()
        print(reader)
    saveButton.config(text="Saved file")
    text.insert(reader)
    saveTo.insert(filePath)
text = tkinter.Text(root, height=15, width=50)
text.grid(row=0, column=0)
saveTo = tkinter.Text(root, height=2, width=50)
saveTo.grid(row=1, column=0)
saveButton = tkinter.Button(root, text="Save file.", command=save)
saveButton.grid(row=2, column=0)
readButton = tkinter.Button(root, text="Read file.", command=readFile)
readButton.grid(row=3, column=0, pady=10)
root.bind("<Control-r>", readFile)
if text.get(1.0, tkinter.END) and saveTo.get(1.0, tkinter.END):
    root.bind("<Control-s>", save)
root.mainloop()
