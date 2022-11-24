from tkinter import *
from registro import *
from area import *

ventana = Tk()
ventana.title("FORMULARIO MAPL")

# plantilla = Frame(ventana, width='1500', height='700')
# plantilla.pack(fill='both', expand='True')
# plantilla.config(bg='red')

zona = Area(ventana=ventana)


# Label(plantilla, text='Selecciona la tabla').place(x=100,y=200)


# ab = StringVar()
# ab.set("asdf")
# Entry(plantilla, textvariable=ab).place(x=400,y=200)

# Button(plantilla, text='Enviarb').place(x=400,y=500)


# abcd = Frame(plantilla, width='1000', height='40')
# abcd.pack()
# abcd.place(x=50,y=200)
# abcd.config(bg='green')


#nuevo_registro = Registro(lista,plantilla,1000)

ventana.mainloop()
