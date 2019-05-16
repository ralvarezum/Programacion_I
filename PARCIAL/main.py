from documento import Documento

doc1 = Documento()
doc1.crear_documento()
doc1.agregar_pagina()
doc1.show()

#Guardado de objetos
import pickle

filehandler = open("Documento.obj","wb")
pickle.dump(doc1,filehandler)
filehandler.close()

file = open("Documento.obj",'rb')
object_file = pickle.load(file)
file.close()

print(object_file.show)
