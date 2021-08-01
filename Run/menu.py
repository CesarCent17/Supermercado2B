from Entidades.entidades import *
from Inputs.opcionesmenu import *
from GestionDatos.gestiondatos import *
from Archivos.archivos import *


class Core:

    def __init__(self):
        self.ent = Entrada() #verifica que sea entero
        self.registrous = [] #creo una lista
        self.menu = Retornodeopcion() #imprime la lista
        self.veri = gestionDatos() #verifica que solo se cree una vez
        self.arch = Archivo()



    def main(self):
        print("\t\t Menu Supermercado")
        listamenu = ("No afiliado", "Afiliado", "Listar", "Salir") #tupla
        opc = self.menu.menuyop(listamenu)

        if opc == 1:
            print("\t\tCrear usuario")
            input("Presione <Enter> para registrarse\n\n")
            self.registro() #nos quedamos aqui
            self.main()

        elif opc == 2:
            print("\n")
            self.afiliado()





        elif opc == 3:
            print("\n")
            self.listar()
            self.main()

        elif opc == 4:
            print("Gracias, tenga un buen dia")


    #Crea el usuario
    def registro(self):
        print("\t\t Registro de usuario")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cedula: ")
        edad = self.ent.Int("Edad: ")
        direccion = input("Direccion: ")
        self.registrous = self.arch.getDatos("Usuario.txt")
        obj = self.veri.Verificar(cedula, self.registrous)
        #Si cedula existe retorna OBJ, SI USUARIO EXISTE
        #si no existe retorna NONE, SI USUARIO NO EXISTE

        #si la cuenta no existe y la cedula es igual a 10 entonces creame la cuenta
        if obj == None and len(cedula) == 10:
            self.user = Usuario(nombre, apellido, cedula, edad, direccion)
            #self.registrous.append(self.user)
            #print("\t\t Cuenta creada con exito! \n\n")
            msg = self.user.nombre + ";" + self.user.apellido\
            + ";" + self.user.cedula + ";" + str(self.user.edad) + ";" + self.user.direccion + ";\n"

            self.arch.crear("Usuario.txt", msg, "a")
            #a es add, w es write,a es sobreescritura, r es read leer

            print("\t\t Cuenta creada con exito! \n\n")


        elif obj == None and len(cedula) != 10:
            print("La cedula ingresada debe tener 10 digitos\n\n")
            self.registro()

        elif obj != None:
            print("\t\tUsted ya esta afiliado \n\n")
            print("Usuario ya existe", obj.getDatos(), "intentelo de nuevo\n")
            input("<Enter para continuar>")



        """if obj != None:
            print("\t\tUsted ya esta afiliado \n\n")
            print("Usuario ya existe", obj.getDatos(),"intentelo de nuevo\n")
            input("<Enter para continuar>")
        self.user = Usuario(nombre, apellido, cedula, direccion, edad)
        self.registrous.append(self.user)
        print("\t\t Cuenta creada con exito! \n\n")"""


    #Funcion afiliado, contiene menuafiliado
    def afiliado(self):
        cedula = input("Ingrese su cedula: ")
        print("\n")
        self.registrous = self.arch.getDatos("Usuario.txt")
        obj = self.veri.Verificar(cedula, self.registrous)
        if obj != None:
            self.menuafiliado(obj, cedula)#nos quedamos aqui

        else:
            print("Usted no esta afiliado")
            input("<Enter para continuar>")
            self.main()

    #Menu afiliado, contiene cuentaexiste y menu de configuracion
    def menuafiliado(self,obj,cedula):
        print("\t\t Menu de afiliado")
        listamenu = ("Consultas", "Configuracion", "Volver")

        #Opciones de menu de afiliado
        opc = self.menu.menuyop(listamenu)

        if opc == 1: #Opcion 1
            print("\n")
            self.cuentaexiste(obj)
            self.main()

        elif opc == 2: #Opcion 2
            self.menusetting(obj,cedula)



        elif opc == 3: #Opcion 3
            print("\n")
            self.main()



    #Menu de configuracion
    def menusetting(self,obj,cedula):
        print("\n")
        print("\t\t Configuracion")
        #self.registrous = self.arch.getDatos("Usuarios.txt")

        #Imprimo el menu
        listamenu = ("Editar", "Eliminar", "Volver")
        opc = self.menu.menuyop(listamenu)

        #Opciones
        if opc == 1:
            print("\n")
            print("\t\t Editar")
            self.editar(obj) #nos quedamos aqui
            self.menusetting(obj,cedula)


        elif opc == 2:
            print("\n")
            print("\t\t Eliminar")
            self.eliminar(cedula, self.registrous, obj)

        elif opc == 3:
            print("\n")
            self.menuafiliado(obj, cedula)

    #Editar los datos generales de la cuenta
    #OJOOOOOOOOOOOOOOOOOOOOOOOO REVISAR BUCLE
    def editar(self, user):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cedula: ")
        edad = self.ent.Int("Edad: ")
        direccion = input("Direccion: ")
        if len(cedula)==10:
            user.nombre = nombre
            user.apellido = apellido
            user.cedula = cedula
            user.edad = edad
            user.direccion = direccion
            msg = ""
            for i in range(len(self.registrous)):
                msg = msg + self.registrous[i].nombre + ";"\
                +self.registrous[i].apellido +";"+self.registrous[i].cedula+";"\
                +str(self.registrous[i].edad)+";"+self.registrous[i].direccion+";\n"

            self.arch.crear("Usuario.txt", msg, "w")
            print("\n")
            print("\t\tDatos actualizados correctamente")
            print(user.getDatos())
            print("\n")

        elif len(cedula) != 10:
            print("La cedula ingresada debe tener 10 digitos\n\n")
            self.editar(user) #prueba







    #Imprime los datos generales de la cuenta
    def cuentaexiste(self, usuario):
        print("\t\tConsulta Datos Generales")
        datos = print(f"\n Nombre: {usuario.nombre}\n Apellido: {usuario.apellido}\
        \n Cedula: {usuario.cedula}\n Edad: {usuario.edad}\n Direccion: {usuario.direccion}\n\n")
        return datos



    #Elimina la cuenta
    def eliminar(self, cedula, lista, obj):
        #self.registrous = self.arch.getDatos("Usuario.txt")
        indice = self.veri.getPosicion(cedula, lista)
        confirma = input("Estas seguro S/N: ")

        #Opciones de eliminar
        if confirma == "S" or confirma == "s": #elimina la cuenta
            print("Elimando cuenta...")
            self.registrous.pop(indice)
            msg = ""
            for i in range(len(self.registrous)):
                msg = msg + self.registrous[i].nombre + ";" \
                      + self.registrous[i].apellido + ";" + self.registrous[i].cedula + ";" \
                      + str(self.registrous[i].edad) + ";" + self.registrous[i].direccion + ";\n"

            self.arch.crear("Usuario.txt", msg, "w")
            print("Cuenta eliminada con exito\n")
            self.main()



        elif confirma == "N" or confirma == "n": #se vuelve a configuracion
            print("Volver")
            print("\n")
            self.menusetting(obj, cedula)

        else:
            print("El caracter no es correcto")
            print("\n")
            self.menusetting(obj, cedula)


    #Muestra los usuarios
    def listar(self):
        print("\t\t Lista de afiliados")
        self.registrous = self.arch.getDatos("Usuario.txt")
        for indice in range(len(self.registrous)):
            print(self.registrous[indice].getDatos())
        print("\n")





