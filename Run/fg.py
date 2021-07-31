class Persona:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula


cadena = "nataly;angulo;0987654321;"
tupla = cadena.split(";")
print(tupla)
# ['nataly', 'angulo', '0987654321', '']

























"""cadena = "cesar;centurion;0987654321;"
tupla = cadena.split(";")
p1 = Persona(tupla[0], tupla[1], tupla[2])
print(tupla)"""