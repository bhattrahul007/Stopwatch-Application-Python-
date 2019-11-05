import sys

try:
    from tkinter import *
    import time
except ImportError:
    from tkinter import *
    import time

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.root = top

        top.geometry("634x314+707+216")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.title("Stopwatch")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.685, relwidth=1.002)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#020202")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.0, rely=0.669, relheight=0.334, relwidth=1.002)
        self.Frame2.configure(relief='flat')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(background="#000000")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        stopwatch = Stopwatch(root)
        stopwatch.pack()

        self.Button1 = Button(self.Frame2, command = stopwatch.Starttime)
        self.Button1.place(relx=0.039, rely=0.286, height=40, width=120)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000000")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {@Microsoft YaHei UI} -size 20 -weight bold")
        self.Button1.configure(foreground="#009500")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''START''')

        self.Button2 = Button(self.Frame2, command = stopwatch.Stoptime)
        self.Button2.place(relx=0.288, rely=0.286, height=40, width=120)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#000000")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {@Microsoft YaHei UI} -size 20 -weight bold")
        self.Button2.configure(foreground="#009500")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''STOP''')

        self.Button3 = Button(self.Frame2, command = stopwatch.Resettime)
        self.Button3.place(relx=0.548, rely=0.286, height=40, width=120)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#000000")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {@Microsoft YaHei UI} -size 20 -weight bold")
        self.Button3.configure(foreground="#009500")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="flat")
        self.Button3.configure(text='''RESET''')

        self.Button4 = Button(self.Frame2, command = stopwatch.Exit)
        self.Button4.place(relx=0.786, rely=0.286, height=40, width=120)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#000000")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {@Microsoft YaHei UI} -size 20 -weight bold")
        self.Button4.configure(foreground="#009500")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(relief="flat")
        self.Button4.configure(text='''EXIT''')

class Stopwatch(Frame):
    def __init__(self, parent, **kwargs):
        self.root = parent
        Frame.__init__(self, parent, kwargs)
        self.starttime = 0.0
        self.nexttime = 0.0
        self.onrunning = 0
        self.timestr = StringVar()
        self.Widgetmaker()

    def Widgetmaker(self):
        stringvar = Label(self, textvariable = self.timestr, font=("times new roman", 80), fg="green", bg="black")
        self.Settime(self.nexttime)
        stringvar.pack(fill=X, expand = NO, pady =2, padx =2)

    def Settime(self, npos):
        hours = int( npos/3600 )
        minutes = int( (npos/60) - hours * 60 )
        seconds = int( npos - minutes * 60)
        milliseconds = int((npos - hours * 3600 - minutes * 60 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d:%02d'%(hours, minutes, seconds, milliseconds))

    def Updater(self):
        self.nexttime = time.time() - self.starttime
        self.Settime(self.nexttime)
        self.timer = self.after(80, self.Updater)

    def Starttime(self):
        if not self.onrunning:
            self.starttime = time.time() - self.nexttime
            self.Updater()
            self.onrunning = 1

    def Stoptime(self):
        if self.onrunning:
            self.after_cancel(self.timer)
            self.nexttime = time.time() - self.starttime
            self.Settime(self.nexttime)
            self.onrunning = 0

    def Resettime(self):
        self.starttime = 0.0
        self.nexttime = 0.0
        self.Settime(self.nexttime)
        self.onrunning = 0

    def Exit(self):
        root.destroy()
        exit()

if __name__ == '__main__':
    root = Tk()
    top = Toplevel1 (root)
    root.mainloop()






