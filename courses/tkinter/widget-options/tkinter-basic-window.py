import tkinter as tk 
LARGE_FONT = ('verdana', 12)

class TestTkinter(tk.Tk):
    # Initalizing class
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Creating a containter and configuring it
        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Setting attributes 
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky='nsew')
        frame.grid(row=110, column = 110, sticky = 'nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Class is assigned to variable label
        label = tk.Label(self, text = 'Start Page', font = LARGE_FONT)
        # Manipulate label
        label.pack(pady = 10, padx = 10)

# Mainloop is a tkinter function
app = TestTkinter()
app.mainloop()