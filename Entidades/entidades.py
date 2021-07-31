class Supermercado:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

        def getDatos(self):
            return self.nombre + " " + self.direccion + "."

class Usuario:
    def __init__(self, nombre, apellido, cedula, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
        self.direccion = direccion


    def getDatos(self):
        return self.cedula + " " + self.nombre + " " + self.apellido +" "\
        + str(self.edad) + " " + self.direccion + "."



