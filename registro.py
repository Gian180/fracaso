from tkinter import *



class Registro:
    
    def __init__(self, lista_registros,tk_panel,pos_y, ancho=1400):
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
       
    def colocar_elementos(self, obj_fram):
         for pos in range(self.tamano):
            
            #Label(obj_fram, text=f'CAMPO {pos}').place(x=self.x,y=self.y)
            po = StringVar()
            entrada = Entry(obj_fram, textvariable=po).place(x=self.x,y=self.y)
            po.set(self.contenido[pos])
            self.x = self.x + self.ancho_box
         Button(obj_fram, text='Actualizar').place(x=self.x,y=self.y)
         self.x = self.x + self.ancho_box
         Button(obj_fram, text='Eliminar').place(x=self.x,y=self.y)

    
    