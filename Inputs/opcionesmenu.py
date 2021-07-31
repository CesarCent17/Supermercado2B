from Inputs.entrada import *
class Retornodeopcion:


    def __init__(self):
        self.checknum = Entrada() #Crear un objeto, verificar numero

    def menuyop(self, listamenu):
        for indice in range(len(listamenu)):
            print(str(indice+1)+".- "+listamenu[indice]+".")



        op = -1 #opcion no valida
        while op < 1 or op > len(listamenu): #mientras me des numeros fuera de rango te pido el numero again
            op = self.checknum.Int("Ingresa una opcion del [1 al" + " " + str(len(listamenu)) + "]: ")

        return op
