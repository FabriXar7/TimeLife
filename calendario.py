# Import Required Library
import tkinter
import tkcalendar
import datetime
import babel.numbers
from tkinter import *
from datetime import datetime
from tkcalendar import Calendar
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("500x500")
root.resizable(0,0)

titulo = tkinter.Label(root, text = "CALCULAR TIEMPO VIVIDO").pack() 
titulo2 = tkinter.Label(root, text = "selecciona fecha de nacimiento").pack() 

# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = 1976, month = 7,
               day = 1)
 
cal.pack(pady = 20)
 
def grad_date():
    inicio = cal.get_date()
    final = str(datetime.now())
    F_inicio = datetime.strptime(inicio, "%m/%d/%y")
    F_final = datetime.strptime(final, "%Y-%m-%d %H:%M:%S.%f")
    date.config(text = "Años: " + str((diff_month(F_final, F_inicio))/12))
    date2.config(text = "Meses: " + str(diff_month(F_final, F_inicio)))
    date3.config(text = "Semanas: " + str((diff_month(F_final, F_inicio))*4))
    date4.config(text = "Dias: " + str((diff_month(F_final, F_inicio))*30))

def salir():
    root.destroy()
    
def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month
    
# Add Button and Label

boton = tkinter.Button(root, text="Calcular", command = grad_date, fg="red")
boton.pack()
boton.place(x=125, y=250)
       
#boton1 = tkinter.Button(root, text="Fecha final", command = grad_date, fg="red")
#boton1.pack()
#boton1.place(x=200, y=250)
       
boton2 = tkinter.Button(root, text="Salir", command = salir, fg="green")
boton2.pack()
boton2.place(x=400, y=400)
 
date = Label(root, text = "")
date.place(x=200, y=270)
date.pack
date2 = Label(root, text = "")
date2.place(x=200, y=300)
date2.pack
date3 = Label(root, text = "")
date3.place(x=200, y=330)
date3.pack
date4 = Label(root, text = "")
date4.place(x=200, y=360)
date4.pack
 
# Execute Tkinter
root.mainloop()