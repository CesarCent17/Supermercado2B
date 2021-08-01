from Entidades.entidades import *



class Archivo:

    def crear(self, nombre, cadena, modo):
        archivo = open(nombre, modo) #funcion que te devuelve un objeto
        archivo.write(cadena)
        archivo.close()

    def getDatos(self, nombre):
        registrous = []
        archivo = open(nombre, "r")
        for linea in archivo.readlines(): #por cada linea haz
            tupla = linea.split(";") #crea una tupla y separa los campos de la linea cuando veas ;

            obj = Usuario(tupla[0], tupla[1], tupla[2], int(tupla[3]), tupla[4])
            registrous.append(obj) #por cada vuelta guardamos el objeto en una lista
        return registrous



