from tkinter import *
from stopwatch import StopwatchApp
import tkinter as tk
from watches import Wat
                                              
window = Tk()
window.title("Умные часы")
window.geometry('300x200')
#def op():
#        watchpro = Wwww()
#        icon = PhotoImage(file = "2978195.png")
#        watchpro.iconphoto(False, icon)
#        watchpro.mainloop()
window['background'] = 'black'
button_1 = Button(text='Часы',background = 'red',foreground='white', width=10, height=5, font=('Roman 10'), command =  Wat)
button_1.place(x=50, y=50)

button_2 = Button(text='Секундомер', background = 'blue',foreground='white', width=12, height=6, font=('Roman 8'),
                  command=StopwatchApp)
button_2.place(x=170, y=50)


icon2 = PhotoImage(file = "2978195.png")
window.iconphoto(True, icon2)



window.mainloop()

