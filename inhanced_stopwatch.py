
#    Nov 07, 2019 10:09:23 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
    import time
except ImportError:
    import tkinter as tk
    import time


class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {Adobe Heiti Std R} -size 23 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("634x314+707+216")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.title("Stopwatch")

        self.Frame1 = tk. Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.685, relwidth=1.002)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#020202")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.669, relheight=0.334, relwidth=1.002)
        self.Frame2.configure(relief='flat')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(background="#000000")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        stopwatch = Stopwatch(top)
        stopwatch.pack()

        self.Button1 = tk.Button(self.Frame2, command = stopwatch.startime)
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

        self.Button2 = tk.Button(self.Frame2, command=stopwatch.stoptime)
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

        self.Button3 = tk.Button(self.Frame2, command=stopwatch.resettime)
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

        self.Button4 = tk.Button(self.Frame2, command=stopwatch.exitapplication)
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


class Stopwatch(tk.Frame):

    def __init__(self, parent = None, **kwargs):
        self.root = parent
        tk.Frame.__init__(self, parent, kwargs)
        self.timestr = tk.StringVar()
        self.onrunning = 0
        self.starttime = 0.0
        self.nexttime = 0.0
        self.widgetsmaker()

    def widgetsmaker(self):
        texting = tk.Label(self, textvariable = self.timestr, font=("times new roman", 80), fg="green", bg="black")
        self.settime(self.nexttime)
        texting.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def settime(self, npos):
        hours = int(npos / 3600)
        minutes = int((npos/60) - (hours*60))
        seconds = int(npos - (hours * 3600) - (minutes * 60))
        milliseconds = int((npos - (hours * 3600) - (minutes * 60) - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d:%02d'%(hours, minutes, seconds, milliseconds))

    def updater(self):
        self.nexttime = time.time() - self.starttime
        self.settime(self.nexttime)
        self.timer = self.after(60, self.updater)

    def startime(self):
        if not self.onrunning:
            self.starttime = time.time() - self.nexttime
            self.updater()
            self.onrunning = 1

    def stoptime(self):
        if self.onrunning:
            self.after_cancel(self.timer)
            self.nexttime = time.time() - self.starttime
            self.settime(self.nexttime)
            self.onrunning = 0

    def resettime(self):
        self.after_cancel(self.timer)
        self.onrunning = 0
        self.starttime = 0
        self.nexttime = 0
        hours = 0
        minutes = 0
        seconds = 0
        milliseconds = 0
        self.timestr.set('%02d:%02d:%02d:%02d'%(hours, minutes, seconds, milliseconds))

    def exitapplication(self):
        self.root.destroy()
        exit()


if __name__ == '__main__':
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()





