from tkinter import Tk, Label, Button 

class MyFirstGUI:
    def __init__(self, master):
        # main root window
        self.master = master
        master.title('A simple GUI')

        # inherits from master - parameter to constructor
        self.label = Label(master, text = 'This is our first GUI')
        self.label.pack()

        self.greet_button = Button(master, text = 'Greet', command = self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text = 'Close', command = master.quit)
        self.close_button.pack()

    def greet(self):
        print('Greetings!')

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

# root window contains all widgets
# set attributes
# set widget (10), layout, event handlers, custom events 
# apply function
# call classes
