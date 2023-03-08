import os
from tkinter import *
from tkinter import font


class Inicio():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("INICIO")
        ancho_ventana = 700
        alto_ventana = 500
        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana.geometry(posicion)
        barra_menus = Menu()
        # Crear el primer menú.
        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_ayuda = Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label="Abrir", command=lambda: self.manejoOpciones(1))
        menu_archivo.add_command(label="Guardar", command=lambda: self.manejoOpciones(2))
        menu_archivo.add_command(label="Guardar Como", command= lambda: self.manejoOpciones(3))
        menu_archivo.add_command(label="Analizar", command=lambda: self.manejoOpciones(4))
        menu_archivo.add_command(label="Errores", command=lambda: self.manejoOpciones(5))
        menu_archivo.add_command(label="Salir", command=self.ventana.destroy)
        menu_ayuda.add_command(label="Manual de Usuario", command=lambda: self.manejoOpciones(6))
        menu_ayuda.add_command(label="Manual Técnico", command=lambda: self.manejoOpciones(7))
        menu_ayuda.add_command(label="Temas de Ayuda",command=lambda: self.manejoOpciones(8))
        # Agregarlo a la barra.
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")

        self.ventana.config(menu=barra_menus)
        self.ventana.configure(bg="pale green")
        self.ventana.resizable(0,0)
        self.ventana.mainloop()

    def manejoOpciones(self, opcion):
        if(opcion == 1):
            print("Opcion 1")
        if(opcion == 2):
            print("Opcion 2")
        if(opcion == 3):
            print("Opcion 3")

        if(opcion == 4):
            print("Opcion 4")
        
        if(opcion == 5):
            print("Opcion 5")
        
        if(opcion == 6):
            print("Opcion 6")

        if(opcion == 7):
            print("Opcion 7")
        
        if(opcion == 8):
            print("Opcion 8")

def main(): 
   app = Inicio()

if __name__ == "__main__":
    main()