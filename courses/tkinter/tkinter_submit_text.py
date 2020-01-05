import tkinter
from tkinter import Tk, PhotoImage, Label, Entry, Button, Text

# ************** Key down function - this will collect the text from the text entry box **************


def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Sorry there is no word like that so please try again"
    output.insert(END, definition)


# ************** Main **************
window = Tk()
window.title('My Computer Science Glossary')
window.configure(background='white')

# ************** My photo **************
photo1 = PhotoImage(file='me.png')
Label(window, image=photo1, bg='black').grid(row=0, column=0, sticky='W')


# ************** Create Label **************
Label(window, text="Enter a word you would like a definition for:", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky='W')


# ************** Create a text entry box **************
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky='W')


# ************** Add a submit button **************
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky='W')

# ************** Create another label **************
Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky='W')

# ************** Create a text box **************
output = Text(window, width=75, height=6, background="white")
output.grid(row=5, column=0, columnspan=2, sticky='W')  # word = WRAP

# ************** Dict **************
my_compdictionary = {
    'algorithm': 'Step by step instructions to complete a task',
    'bug': 'Piece of code that causes a program to fail'
}

# ************** Exit Label **************
Label(window, text="Click to Exit:", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky='W')


# ************** Exit button **************
Button(window, text="EXIT", width=14).grid(row=7, column=0, sticky='E')  # command=close_window

# ************** Exit function **************


def close_window():
    window.destroy()
    exit

# ************** Run the main loop **************


window.mainloop()
