import tkinter as tk
import tkinter.ttk as ttk

from collections import OrderedDict
from PIL import ImageTk,Image
import subprocess
import queue
import os
from threading import Thread

class UI(tk.Tk):
    """
    Main Class that initiates and control the UI
    """
    def __init__(self, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)

        self.attributes('-fullscreen', True)

        # Create a container frame to hold all the pages inside it
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = OrderedDict()
        self.current_frame=None

        self.create_frames(container)

        self.frames_list = list(self.frames.keys())
        self.current_frame_index = 0
        self.show_frame('StartPage')

    def create_frames(self,container):
        start_page_frame = StartPage(container, self)
        self.frames['StartPage'] = start_page_frame
        start_page_frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont, data=None):
        """
        Display the given frame
        :param cont:
        :return:
        """
        frame = self.frames[cont]
        self.current_frame = cont
        print("current frame is",cont)
        frame.tkraise()
        return frame

    def reset(self):
        self.show_frame(self.frames_list[0])



class StartPage(tk.Frame):
    """
    Start page frame Class
    """
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent)

        menubar = MenuBar(self, controller)
        controller.config(menu=menubar)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.left_frame = LeftFrame(self, controller)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = Console(self, controller)
        self.right_frame.grid(row=0, column=1)




class LeftFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)

        self.progress_bars = []
        self.enable = True

        start_button = tk.Button(self, text="Start", command=self.start)
        img = Image.open("start-job-icon.png")
        self.start_photoimage = ImageTk.PhotoImage(img)
        start_button.config(image=self.start_photoimage, width=100, height=90,borderwidth=0, highlightthickness=0, padx=0, pady=0)
        start_button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        stop_button = tk.Button(self, text="Stop", command=self.stop)
        img = Image.open("pause2.png")
        self.stop_photoimage = ImageTk.PhotoImage(img)
        stop_button.config(image=self.stop_photoimage, width=120, height=120, borderwidth=0, highlightthickness=0, padx=0, pady=0)
        stop_button.grid(row=0, column=1, padx=20, pady=20, columnspan=3, sticky="nsew")


        ingestion_label = tk.Label(self, text="INGESTION", borderwidth=2, relief="groove", pady=20, width=15)
        ingestion_label.grid(row=1, column=0, pady=10)
        self.ingestion_progress=ttk.Progressbar(self,orient=tk.HORIZONTAL,length=150,mode='determinate')
        self.ingestion_progress.grid(row=1, column=1)
        self.ingestion_progress['value'] = 0
        self.progress_bars.append(self.ingestion_progress)

        preprocessing_label = tk.Label(self, text="PRE-PROCESSING", borderwidth=2, relief="groove", pady=20, width=15)
        preprocessing_label.grid(row=2, column=0, pady=10)
        self.preprocessing_progress=ttk.Progressbar(self,orient=tk.HORIZONTAL,length=150,mode='determinate')
        self.preprocessing_progress.grid(row=2, column=1)
        self.preprocessing_progress['value'] = 0
        self.progress_bars.append(self.preprocessing_progress)

        processing_label = tk.Label(self, text="PROCESSING", borderwidth=2, relief="groove", pady=20, width=15)
        processing_label.grid(row=3, column=0, pady=10)
        self.processing_progress=ttk.Progressbar(self,orient=tk.HORIZONTAL,length=150,mode='determinate')
        self.processing_progress.grid(row=3, column=1)
        self.processing_progress['value'] = 0
        self.progress_bars.append(self.processing_progress)

        eda_label = tk.Label(self, text="EDA", fg="black", borderwidth=2, relief="groove", pady=20, width=15)
        eda_label.grid(row=4, column=0, pady=10)
        self.eda_progress=ttk.Progressbar(self,orient=tk.HORIZONTAL,length=150,mode='determinate')
        self.eda_progress.grid(row=4, column=1)
        self.eda_progress['value'] = 0
        self.progress_bars.append(self.eda_progress)

        select_model_label = tk.Label(self, text="SELECT MODEL", borderwidth=2, relief="groove", pady=20, width=15)
        select_model_label.grid(row=5, column=0, pady=10)
        self.select_model_progress=ttk.Progressbar(self,orient=tk.HORIZONTAL,length=150,mode='determinate')
        self.select_model_progress.grid(row=5, column=1)
        self.select_model_progress['value'] = 0
        self.progress_bars.append(self.select_model_progress)

        train_model_label = tk.Label(self, text="TRAIN MODEL", borderwidth=2, relief="groove", pady=20, width=15)
        train_model_label.grid(row=6, column=0, pady=10)
        self.train_model_progress=ttk.Progressbar(self,orient=tk.HORIZONTAL,length=150,mode='determinate')
        self.train_model_progress.grid(row=6, column=1)
        self.train_model_progress['value'] = 0
        self.progress_bars.append(self.train_model_progress)

        dbpush_label = tk.Label(self, text="DATABASE PUSH", borderwidth=2, relief="groove", pady=20, width=15)
        dbpush_label.grid(row=7, column=0, pady=10)
        self.dbpush_progress=ttk.Progressbar(self,orient=tk.HORIZONTAL,length=150,mode='determinate')
        self.dbpush_progress.grid(row=7, column=1)
        self.dbpush_progress['value'] = 0
        self.progress_bars.append(self.dbpush_progress)



    def start(self):
        print("started")
        self.enable = True
        self.parent.right_frame.start()

        for bar in self.progress_bars:
            bar['value']=0

        for bar in self.progress_bars:
            if not self.enable :
                break
            for i in range(4):
                if not self.enable :
                    break
                bar['value']+=25
                self.controller.after(500)
                self.controller.update()



    def stop(self):
        self.enable = False
        self.parent.right_frame.stop()
        print("stopped")


class MenuBar(tk.Menu):
    def __init__(self,master,controller, **kw):
        tk.Menu.__init__(self, master, kw)

        filemenu = FileMenu(self, controller)
        self.add_cascade(label="File", menu=filemenu)

        editmenu = EditMenu(self, controller)
        self.add_cascade(label="Edit", menu=editmenu)

        helpmenu = HelpMenu(self, controller)
        self.add_cascade(label="Help", menu=helpmenu)


class FileMenu(tk.Menu):
    def __init__(self, master,controller, **kw):
        tk.Menu.__init__(self, master, kw, tearoff=0)

        self.add_command(label="New", command=self.new)
        self.add_command(label="Open", command=self.open)
        # self.add_command(label="Save", command=self.save)
        # self.add_command(label="Save as...", command=self.save_as)
        # self.add_command(label="Close", command=self.close)
        self.add_separator()
        self.add_command(label="Exit", command=controller.quit)

    def new(self):
        print("new")

    def open(self):
        print("open")

class EditMenu(tk.Menu):
    def __init__(self, master,controller, **kw):
        tk.Menu.__init__(self, master, kw, tearoff=0)

        self.add_command(label="Undo", command=self.undo)
        self.add_separator()
        self.add_command(label="Cut", command=self.cut)
        # self.add_command(label="Copy", command=self.copy)
        # self.add_command(label="Paste", command=self.paste)
        # self.add_command(label="Delete", command=self.delete)
        # self.add_command(label="Select All", command=self.select_all)

    def undo(self):
        print("undo")

    def cut(self):
        print("cut")


class HelpMenu(tk.Menu):
    def __init__(self, master, controller, **kw):
        tk.Menu.__init__(self, master, kw, tearoff=0)

        self.add_command(label="Help Index", command=self.help_index)
        self.add_command(label="About...", command=self.about)

    def help_index(self):
        print("Help Index")

    def about(self):
        print("about")


class Console(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.createWidgets()

    def start(self):
        consolePath = "console.py"
        self.p = subprocess.Popen(["python",consolePath],
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE,
                                  stderr=subprocess.PIPE)

        # make queues for keeping stdout and stderr whilst it is transferred between threads
        self.outQueue = queue.Queue()
        self.errQueue = queue.Queue()

        # keep track of where any line that is submitted starts
        self.line_start = 0

        # make the enter key call the self.enter function
        self.ttyText.bind("<Return>",self.enter)

        # a daemon to keep track of the threads so they can stop running
        self.alive = True
        # start the functions that get stdout and stderr in separate threads
        Thread(target=self.readFromProccessOut).start()
        Thread(target=self.readFromProccessErr).start()

        # start the write loop in the main thread
        self.writeLoop()

    def stop(self):
        self.alive=False
        # write exit() to the console in order to stop it running
        self.p.stdin.write("exit()\n".encode())
        self.p.stdin.flush()

    def destroy(self):
        "This is the function that is automatically called when the widget is destroyed."
        self.stop()
        # call the destroy methods to properly destroy widgets
        self.ttyText.destroy()
        tk.Frame.destroy(self)

    def enter(self,e):
        "The <Return> key press handler"
        string = self.ttyText.get(1.0, tk.END)[self.line_start:]
        self.line_start+=len(string)
        self.p.stdin.write(string.encode())
        self.p.stdin.flush()

    def readFromProccessOut(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.p.stdout.raw.read(1024).decode()
            self.outQueue.put(data)

    def readFromProccessErr(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.p.stderr.raw.read(1024).decode()
            self.errQueue.put(data)

    def writeLoop(self):
        "Used to write data from stdout and stderr to the Text widget"
        # if there is anything to write from stdout or stderr, then write it
        if not self.errQueue.empty():
            self.write(self.errQueue.get())
        if not self.outQueue.empty():
            self.write(self.outQueue.get())

        # run this method again after 10ms
        if self.alive:
            self.after(10,self.writeLoop)


    def write(self,string):
        self.ttyText.insert(tk.END, string)
        self.ttyText.see(tk.END)
        self.line_start+=len(string)
        self.controller.update()

    def createWidgets(self):
        self.ttyText = tk.Text(self, wrap=tk.WORD)
        self.ttyText.pack(fill=tk.BOTH,expand=True)



app = UI()
app.mainloop()