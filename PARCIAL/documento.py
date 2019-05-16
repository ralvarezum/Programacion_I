from pagina import Pagina
import os

class Documento():
    def __init__(self):
        self.paginas = []
        self.nombre = ""
    
    def crear_documento(self):
        archivo = input("Ingrese el nombre del documento: ")
        self.nombre = archivo
        f = open(self.nombre,'w')
        f.close()
        print(f"El archivo {archivo} fue creado con exito!")

    def agregar_pagina(self):
        self.paginas = Pagina()
        self.paginas.agregar_encabezado(self.nombre)
        self.paginas.agregar_parrafo(self.nombre)
        self.paginas.agregar_pie(self.nombre)

    def show(self):
        try:
            f = open(self.nombre, 'r')
            text = f.read()
            #f = os.popen(self.nombre, 'r')
            print(text)
        except IOError:
            print("Error en la lectura del archivo" + self.nombre)
