from tkinter import *
from time import strftime
from datetime import datetime, timedelta

class Wat(Tk):
    def __init__(self):
        super().__init__()
        self.title('Цифровые часы')
        self["background"] = 'black'
        self.lable = Label(self, font=('aerial', 30), background='black', foreground='white')
        self.lable2 = Label(self, font=('aerial', 30), background='black', foreground='blue')
        self.lable3 = Label(self, font=('aerial', 30), background='black', foreground='red')

        self.time()

        
    def time(self):
        now = datetime.today() 
        #string = now.strftime('%H:%M:%S %p')
        #self.lable.config(text=string)
        self.lable["text"] = now.strftime('%H:%M:%S %p') + " (IRK)"
        self.lable.after(1000, self.time)
        self.lable.pack(anchor='center')
        now = datetime.today() - timedelta(hours = 5)
        self.lable2["text"] = now.strftime('%H:%M:%S %p') + " (МСК)"
        self.lable2.pack(anchor='center')
        now2 = datetime.today() - timedelta(hours = 3)
        self.lable3["text"] = now2.strftime('%H:%M:%S %p') + " (EKB)"
        self.lable3.pack(anchor='center')
        
        

if (__name__ == "__main__"):
    root = Wat()
    icon3 = PhotoImage(file = "www.png")
    root.iconphoto(False, icon3)
    root.mainloop()
