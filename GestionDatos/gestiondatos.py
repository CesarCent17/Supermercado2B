class gestionDatos:
    def Verificar(self, cedula, lista):
        obj = None
        for indice in range(len(lista)):
            if cedula == lista[indice].cedula:
                obj = lista[indice]
                break

        return obj

    def getPosicion(self, cedula, lista):
        pos = -1
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                pos = i
                break
        return pos


