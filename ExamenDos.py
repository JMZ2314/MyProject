# Jhonmaiker Zerpa
# Usuario administrador : maiker.zerpac@gmail.com - JM2001
class registro():

    def registrar(self):
        self.nombre= input("Ingrese su nombre: ")
        self.apellido = input ("Ingrese su apellido: ")
        while True :
            self.correo = input("Correo electronico: ")
            if self.Comprobar(self.correo) == True :
                print("Este correo ya fue registrado")
                print("")
            else:
                break
        self.contraseña=input("Contraseña: ")
        file = open ("registrados.txt","a")
        file.write(self.nombre +  " - " +  self.apellido + " - " + self.correo + " - " + self.contraseña + "\n" )
        file.close()

    def Comprobar(self,cadena):
        valor = False
        archivo = open ("registrados.txt","r")
        for linea in archivo:
            if cadena in linea :
                valor = True;
                break
        archivo.close()
        return valor

    def comprobarAdmin(self,correo,contraseña):
        if correo =="maiker.zerpac@gmail.com"  and  contraseña == "JM2001" :
            return True
        else:
            return False
        
    def UsuarioAdmin(self):
        file = open("registrados.txt","r")
        linea = file.read()
        file.close()
        print("")
        print("     -USUARIOS REGISTRADOS-     ")
        print("_________________________________")
        print(linea)


    def suma (self,a,b):
        print("Resultado = ",a+b)

    def resta (self,a,b):
        print("Resultado = ",a-b)
        

    def multiplicacion(self,a,b):
        print("Resultado = ",a*b)

    def division(self,a,b):
        print("Resultado = ", a/b)
    
    
            


numUno=0
numDos = 0
opc1=0
opc2 =0
usuario = registro()

while opc1 != 3 :
    
    print()
    print("1.Iniciar sesion")
    print("2.Registrar un nuevo usuario")
    print("3.Salir")
    print("")
    opc1 = int (input ("Opcion: "))
    print("")

    if opc1 == 1 :
        while True :
            correo = input ("Correo: ")
            contraseña = input("Contraseña: ")
            if usuario.comprobarAdmin(correo,contraseña) == True :
                usuario.UsuarioAdmin()
            if usuario.Comprobar(correo)== True and usuario.Comprobar(contraseña) == True:
                while opc2 != 5 :
                    print("")
                    print("1.Suma")
                    print("2.Resta")
                    print("3.Multiplicacion")
                    print("4.Division")
                    print("5.Volver al menu principal")
                    print("")
                    opc2 = int(input("Opcion: "))
                    print("")
                    if opc2 == 1 :
                        numUno = int (input("Valor 1: "))
                        numDos = int (input ("Valor 2 :"))
                        usuario.suma(numUno,numDos)
                    elif opc2 == 2 :
                        numUno = int (input("Valor 1: "))
                        numDos = int (input ("Valor 2 :"))
                        usuario.resta(numUno,numDos)
                    elif opc2 == 3 :
                        numUno = int (input("Valor 1: "))
                        numDos = int (input ("Valor 2 :"))
                        usuario.multiplicacion(numUno,numDos)
                    elif opc2 == 4:
                        numUno = int (input("Valor 1: "))
                        numDos = int(input ("Valor 2 :"))
                        usuario.division(numUno,numDos)
                break
            elif usuario.Comprobar(correo)== False:
                print("El correo no esta registrado" + "\n")
                break
            elif usuario.Comprobar(contraseña)== False:
                print("Contraseña invalida" + "\n")
                break
            
           
    elif opc1 == 2 :
        usuario.registrar()
        


        
