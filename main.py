from tkinter import *
import tkinter.font as tkFont

class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.createWidgets()
        self.alarm_id = None
        self._paused = False
        self._starttime = 0

    def createWidgets(self):
        fonttxt = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
        
        self.label=Label(self,text="Enter the time in seconds for the timer : ",font=fonttxt)
        self.label.grid(row=0,column=0)

        self.minute=StringVar()
        self.minute.set("00")
        self.minuteEntry= Entry(self,text=self.minute, font=fonttxt)
        self.minuteEntry.grid(row=0,column=1)
        
        self.startButton = Button(self, text="Start", font=fonttxt,command=self.startTime)
        self.startButton.grid(row=1,column=0)

        self.stopButton = Button(self, text="Stop", font=fonttxt, command=self.stopTime)
        self.stopButton.grid(row=1,column=1)

        self.resetButton = Button(self, text="Reset", font=fonttxt, command=self.resetTime)
        self.resetButton.grid(row=1,column=2)

        self.label2=Label(self,text="Timer Finished",font=fonttxt)
        self.label2.grid(row=3,column=0)
        self.label2.grid_remove()
        self.update()
    def startTime(self):
        self._paused = False
        if self.alarm_id is None:
            self.countdown(int(self.minuteEntry.get()))

    def stopTime(self):
        if self.alarm_id is not None:
            self._paused = True

    def resetTime(self):
        if self.alarm_id is not None:
            self.master.after_cancel(self.alarm_id)
            self.alarm_id = None
            self._paused = False
            self.minute.set("00")
            self.label2.grid_remove()
            self._paused = True

    def countdown(self, timeInSeconds, start=True):
        if start:
            self._starttime = timeInSeconds
        if self._paused:
            self.alarm_id = self.master.after(1000, self.countdown, timeInSeconds, False)
        else:
            mins, secs = divmod(timeInSeconds, 60)
            timeformat = "{0:02d}:{1:02d}".format(mins, secs)
            app.minute.set(timeformat)
            print(self.minuteEntry.get())
            if(self.minuteEntry.get()=="00:00"):
                self.label2.grid()
                return
            self.alarm_id = self.master.after(1000, self.countdown, timeInSeconds-1, False)


if __name__ == '__main__':
    win = Tk()
    win.title("Timer")
    win.geometry("600x400")
    app = App(win)
    win.mainloop()