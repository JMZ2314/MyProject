class persona():
    def registrar (self):
        self.nombre = str(input ("Ingrese su nombre: "))
        while self.nombre.isalpha() != True :
            print("Ingrese solo letras")
            print("")
            self.nombre = str(input ("Ingrese su nombre: "))


        self.apellido = str(input ("Ingrese su apellido: "))
        while self.apellido.isalpha() != True :
            print("Dato invalido !!!!!!!!")
            print("")
            self.apellido = str(input ("Ingrese su apellido: "))

        while True :
            try:
                self.edad = int(input ("Edad: "))
                break
            except:
                print("Esto no es numero amigo")
                print("")

class niños(persona):

    def registrarNiño(self):
        self.registrar()

        self.juguete = str(input("Juguete Favorito: "))
        while self.juguete.isalpha() != True :
            print("Esta seccion solo acepta letras")
            print("")
            self.juguete = str(input("Juguete Favorito: "))

        self.color = str(input("Color: "))

        while self.color.isalpha() != True :
            print("Esta seccion solo acepta letras")
            print("")
            self.color = str(input("Color: "))
            


class adulto(persona):
    def registrarAdulto(self):
        self.registrar()
        self.correo = input("Correo: ")
        while True :
            try :
                self.cedula = int (input ("Cedula: "))
                break
            except:
                print("Ingrese solo numeros")


listaniños = []
listaadultos = []

opc = ""

while opc != "3" :

    print("")
    print("1.Registrar")
    print("2.Mostrar registrados")
    print("3.Salir")
    print("")
    opc = input ("Opcion: ")

    if opc == "1" :
        opc = ""
        print("")
        print("1.Niño")
        print("2.Adulto")
        print("")
        opc = input("Opcion: ")
        print("")

        if opc == "1" :
            usuarioN = niños ()
            usuarioN.registrarNiño()
            listaniños.append(usuarioN)
        elif opc == "2" :
            usuarioA = adulto()
            usuarioA.registrarAdulto()
            listaadultos.append(usuarioA)
    elif opc == "2" :
        print("           NIÑOS         ")
        print("___________________________")
        for i in listaniños :
            print("-" + " " + i.nombre + " "  + i.apellido + " " + str(i.edad) + " " + i.juguete)
 
        print("")
        print("           ADULTOS       ")
        print("____________________________")
        for i in listaadultos :
            print( "-" + " " + i.nombre + " " + i.apellido + " " + " " + str(i.edad) + " " + i.correo)
