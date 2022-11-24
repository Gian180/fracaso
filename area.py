from tkinter import ttk
from tkinter import *
from registro import *
from database import DataBase

OPCIONES = ['clientes', 'usuarios']

class Area(DataBase):
    esquema = DataBase()
    tabla_name = "usuarios"
    lista_objetos_registro = []
    




    def __init__(self,ventana):
        super().__init__()
        self.plantilla = Frame(ventana, width='1500', height='700')
        self.plantilla.pack(fill='both', expand='True')
        self.plantilla.config(bg='DeepSkyBlue4')

        self.valores = ['uno','dos','tres']

        self.contenedor = Frame(self.plantilla, width='1500', height='400')
        self.contenedor.place(x=5,y=200)
        self.contenedor.config(bg='Cyan4')

        self.current_var = StringVar()
        self.opciones = ttk.Combobox(ventana,width='40')
        self.opciones.place(x=500,y=20)
        self.opciones['values'] = OPCIONES
        self.opciones['state'] ='readonly'

        Button(self.plantilla, text='VER DATOS', command=self.cambiar_lista_registros).place(x=850,y=20)

        self.resultado = Area.esquema.get_data_DB(Area.tabla_name)

        self.generar_lista()

    def dibujar_area(self, pos_y,lista_data):
        nuevo_registro = Registro(lista_data,self.contenedor,pos_y)
        return nuevo_registro

    #GENERA es espacio donde estan los registros
    def generar_lista(self):
        self.lugar_y = 10
        for reg in self.resultado:
            self.nuevo = self.dibujar_area(self.lugar_y , reg)
            self.lugar_y = self.lugar_y + 30            
            Area.lista_objetos_registro.append(self.nuevo)


    # def CambiarColor(self):
    #     self.color = self.opciones.get()
    #     self.plantilla.config(bg=F'{self.color}')



    def cambiar_lista_registros(self):
        self.contenedor.destroy()
        self.contenedor = Frame(self.plantilla, width='1500', height='400')
        self.contenedor.place(x=5,y=200)
        self.contenedor.config(bg='Cyan4')

        self.resultado = Area.esquema.get_data_DB(self.opciones.get())

        self.generar_lista()
    