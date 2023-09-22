## What is this?

This is a notepad project created with code from
* [StackOverflow](https://www.stackoverflow.com)
* [The python codes](thepythoncodes.com)
* [Geeks for geeks](geeksforgeeks.org)
and [Python Tkinter Document](https://docs.python.org/3/library/tkinter.html).

this program mainly uses tkinter and it's modules, and no modules imported
in this program require an external installation.
inside the file `notepadGUI.py`, you will find a class called `NotepadRun`.
It was originally a normal program with function, but for better editing of
methods, I converted it to a class.

This class is dependent on outside frames, for example, the mainframe
tkinter window when it starts, and the text widgets, are created outside
the class, and needed to be provided as a parameter to `NotepadRun.__init__`
method.

There is another file, called `syntax_checker.py` , which is important when
accessing the 'NotepadRun.programmerMode' method.

As the name of the object describes, it not essentially acts as a basic IDE,
providing help with the automatic quotation and bracket closing, and a basic,
keyword highlighter, which highlights the function and keywords so on and so
forth.

There is also another purpose for this, that is doing the highlighting for
the spellchecking, how it gets the dictionary to check with, is documented
below.

There is one text file, named as `spellcheck.txt`, which has over 450000+
words. It is used as a spell checker, which provides Microsoft Word's typo functionality.

You can edit the class by overriding methods, but be careful since these
methods are interlinked like crazy, and you might break stuff while doing so.
so beware when editing the class or overriding in your program.


## Documentation

1.  First, make sure you have setuptools upgraded (to check that, run the command
`pip install --upgrade setuptools` in your terminal.)

2. Install the wheel. **DO NOT edit the name of file!**

3. Now use the library. you do this if you want to use it
to do the import, type in `import NotepadGUI.notepadGUI as notepad`.
now paste in this code to generate the base for this class that will lateron use this.
of course, you can edit this to your liking, perhaps change the font and size? maybe bold? italics? name it.
```python3
def main():
    """ main """
    root = tkinter.Tk()
    root.title("Notepad GUI v3.0 STABLE")
    text = tkinter.Text(root, height=20, width=100,
                        font=("Arial Rounded MT Bold",
                              18), )
    text.grid(row=0, column=0, pady=10)
    saveTo = tkinter.Text(root, height=2, width=50,
                          font=("Arial Rounded MT Bold",
                                12))
    saveTo.grid(row=1, column=0)
    notepad.NotepadRun(text_box=text, gui=root, saveTo=saveTo)


if __name__ == "__main__":
    main()
```

Now this program should run. 
You can, as mentioned, email me for reporting bugs and features. 
And I also will update in the drive folder, so you always test the newest version!

That's basically it!
Have a great day :D
-A normal high school student
