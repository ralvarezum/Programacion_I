class Parrafo():
    def __init__(self):
        self.lineas = []

    def agregar_lineas(self,nombre):
        entry = ""
        bucle = True
        while bucle:
            print("Ingrese el parrafo: \n")
            while entry != "done":
                self.lineas.append(entry)
                entry = input("")
            self.lineas = ''.join(self.lineas)
            f = open(nombre, 'a')
            f.write(self.lineas + "\n\n")
            f.close()
            #NO FUNCIONA CON MAS DE 1 PARRAFO
            respuesta = input("Quiere agregar otro parrafo ///S=SI N=NO///")

            if(respuesta.capitalize()) == 'N':
                bucle = False
            else:
                entry = ""
