class Entrada:

    def Int(self, msg):
        while True:
            try:
                n = int(input(msg))
                break
            except ValueError:
                print("Error Ingrese un numero entero: ")
        return n






