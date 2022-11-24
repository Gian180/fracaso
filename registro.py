from tkinter import *
from database import DataBase


class Registro:

    nombre_tabla_registro = ""
    
    def __init__(self, lista_registros,tk_panel,pos_y,nombre_tabla, ancho=1400 ):
        Registro.nombre_tabla_registro = nombre_tabla
        self.contenido = lista_registros
        self.id = lista_registros[0]
        self.frame_registro = Frame(tk_panel , width=ancho, height='30')
        self.frame_registro.config(bg='DeepSkyBlue4')
        self.frame_registro.pack()
        self.frame_registro.place(x=50,y=pos_y)
        self.tamano = len(lista_registros)
        self.x = 0
        self.y = 0
        self.ancho_box = ancho/(self.tamano + 2)
        self.colocar_elementos(self.frame_registro)

        self.ejecutor_registro = DataBase()
       
    def colocar_elementos(self, obj_fram):
         for pos in range(self.tamano):
            
            #Label(obj_fram, text=f'CAMPO {pos}').place(x=self.x,y=self.y)
            po = StringVar()
            entrada = Entry(obj_fram, textvariable=po).place(x=self.x,y=self.y)
            po.set(self.contenido[pos])
            self.x = self.x + self.ancho_box
         Button(obj_fram, text='Actualizar', command=self.boton_actualizar).place(x=self.x,y=self.y)
         self.x = self.x + self.ancho_box
         Button(obj_fram, text='Eliminar', command=self.boton_eliminar).place(x=self.x,y=self.y)



    
    def boton_actualizar(self):
        print(f"ACTUALIZANDO {self.id} en {Registro.nombre_tabla_registro}")
        

    
    def boton_eliminar(self):
        
        self.ejecutor_registro.delete_data(Registro.nombre_tabla_registro,self.id )

        print(f"eliminando {self.id} en {Registro.nombre_tabla_registro}")