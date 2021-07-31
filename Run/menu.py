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
        self.registrous = self.arch.getDatos("Usuarios.txt")
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

            self.arch.crear("Usuarios.txt", msg, "a")
            #a es add, w es write,a es sobreescritura, r es read leer

            print("\t\t Cuenta creada con exito! \n\n")


        elif obj == None and len(cedula) != 10:
            print("La cedula tiene 10 digitos, por favor vuelta a intentarlo")
            #self.registro()

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
        obj = self.veri.Verificar(cedula, self.registrous)
        if obj != None:
            self.menuafiliado(obj, cedula)#nos quedamos aqui

        else:
            print("Usted no esta afiliado")
            input("<Enter para continuar>")
            self.main()
            #ERROR


    #Imprime los datos generales de la cuenta
    def cuentaexiste(self, usuario):
        print("\t\tConsulta Datos Generales")
        datos = print(f"\n Nombre: {usuario.nombre}\n Apellido: {usuario.apellido}\
        \n Cedula: {usuario.cedula}\n Edad: {usuario.edad}\n Direccion: {usuario.direccion}\n")
        return datos

    #Editar los datos generales de la cuenta
    def editar(self, usuario):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cedula: ")
        edad = self.ent.Int("Edad: ")
        direccion = input("Direccion: ")
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.cedula = cedula
        usuario.edad = edad
        usuario.direccion = direccion
        print("\n")
        print("\t\tDatos actualizados correctamente")
        print(usuario.getDatos())
        print("\n")

    #Elimina la cuenta
    def eliminar(self, cedula, lista, obj):
        indice = self.veri.getPosicion(cedula, lista)
        confirma = input("Estas seguro S/N: ")

        #Opciones de eliminar
        if confirma == "S" or confirma == "s": #elimina la cuenta
            print("Elimando cuenta...")
            print("Cuenta eliminada con exito\n")
            self.registrous.pop(indice)
            self.main()



        elif confirma == "N" or confirma == "n": #se vuelve a configuracion
            print("Volver")
            print("\n")
            self.menusetting(obj, cedula)

        else:
            print("El caracter no es correcto")
            print("\n")
            self.menusetting(obj, cedula)


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
            self.menusetting(obj,cedula)  #nos quedamos aqui



        elif opc == 3: #Opcion 3
            print("\n")
            self.main()




    #Menu de configuracion
    def menusetting(self,obj,cedula):
        print("\n")
        print("\t\t Configuracion")

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



    #Muestra los usuarios
    def listar(self):
        print("\t\t Lista de afiliados")
        for indice in range(len(self.registrous)):
            print(self.registrous[indice].getDatos())
        print("\n")







