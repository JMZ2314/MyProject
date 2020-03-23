# JHONMAIKER ZERPA

class persona():
    
    def registrar(self):

        self.nombre = input("Nombre: ")
        while self.nombre.isalpha() != True:
            print("Ingrese solo letras!" + "\n")
            self.nombre = input("Nombre: ")
        
        self.apellido = input("Apellido: ")
        while self.apellido.isalpha()!= True:
            print("Ingrese solo letras!" + "\n")
            self.apellido = input("Apellido: ")
            
        self.pais = input("Pais de residencia: ")
        while self.pais.isalpha() != True:
            print("Ingrese solo letras!")
            self.pais = input("Pais de residencia: ")
            
        while True:
            self.genero = input("Genero M/F : ")
            if self.genero == "M" or self.genero=="m" or self.genero=="F" or self.genero=="f":
                break
            else :
                print("Opcion no valida" + "\n")
        self.estatus=False
        self.enfermedad= ""
        

class Niños(persona):
    def registrarNiños(self):
        self.registrar()
        while True :
            try:
                self.edad= int(input("Edad: "))
                if self.edad > 5 and  self.edad <= 18:
                    break
                else:
                    print("Debe tener entre 5 y 18 años" + "\n")
            except:
                print("Solo puede ingresar numeros" + "\n")

class Adultos(persona):

    def registrarAdultos(self):
        self.registrar()
        while True:
            try:
                self.edad = int (input("Edad: "))
                if self.edad >= 18  and self.edad < 60:
                    break
                else:
                    print("Debe tener entre 18 y 60 años")
            except:
                print("Debes ingresar solo numeros" + "\n")


class Ancianos(persona):
    def registrarAncianos(self):
        self.registrar()
        while True:
            try:
                self.edad = int(input("Edad: "))
                if self.edad >= 60:
                    break
                else:
                    print("Debe tener un minimo de 60 años" + "\n")
            except:
                print("Debe ingresar solo numeros!" + "\n")

        print("\n"+ "¿Posee alguna condicion? S/N" )
        while True:
            opc = input("R: ")
            if opc.upper() == "S" or opc.upper() == "N":
                break
            else:
                print("Opción no valida!" + "\n")
        if opc.upper() == "S":
            self.condicion = input("Condicion: ")
            while self.condicion.isalpha() !=  True:
                print("Debe ingresar solo letras" + "\n")
                self.condicion = input("Condicion:")


def MostrarAdultos(lista):
    contador = 1
    print("")
    print("|||ADULTOS|||" + "\n")
    for i in lista:
        if i.edad >= 18 and i.edad < 60:
            print(str(contador) + "." + i.nombre,i.apellido,i.edad,i.enfermedad,i.pais)
            contador = contador + 1
    print("")

def MostrarNiños(lista):
    contador = 1
    print("")
    print("|||NIÑOS|||" + "\n")
    for i in lista:
        if i.edad < 18 :
            print(str(contador) + "." + i.nombre,i.apellido,i.edad,i.enfermedad,i.pais)
            contador = contador + 1
    print("")

def MostrarMayores(lista):
    contador = 1
    print("")
    print("|||MAYORES DE EDAD|||" + "\n")
    for i in lista:
        if i.edad >=60:
            print(str(contador) + "." + i.nombre,i.apellido,i.edad,i.enfermedad,i.pais)
            contador = contador + 1
    print("")

def MostrarMujeres(lista):
    contador = 1
    print("")
    print("|||MUJERES|||" + "\n")
    for i in lista:
        if i.genero == "f" or i.genero == "F":
            print(str(contador)+ "." + i.nombre,i.apellido,i.edad,i.enfermedad,i.pais)
            contador = contador + 1
    print("")
        
def MostrarHombres(lista):
    contador = 1
    print("")
    print("|||HOMBRES|||" + "\n")
    for i in lista:
        if i.genero == "m" or i.genero == "M":
            print(str(contador) + "." + i.nombre,i.apellido,i.edad,i.enfermedad,i.pais)
    print("")
    
def MostrarEspecifico(lista,pais):
    contador = 1
    print("")
    for i in lista:
        if i.pais.lower() == pais.lower():
            print(str(contador) + "."+ i.nombre, i.apellido, i.edad,i.enfermedad)
            contador = contador + 1
    print("")


def Menu():
    print("")
    print("Escriba  los sintomas que presenta: " + "\n")
    print("1.Fiebre              2.Secresion Nasal")
    print("3.Tos seca            4.Dificultad para respirar")
    print("5.Fatiga              6.Tos con Flema")
    print("7.Congestion Nasal    8.Malestar General")
    print("9.Escalofrios         10.Molestias de Garganta")
    print("11.Nariz Irritada     12.Sarpullido")
    print("13.Finalizar" + "\n")
    print("Ingrese '13' si no presenta mas sintomas" + "\n")


def paises(objeto,lista):
    if not objeto.pais.lower() in lista:
        lista.append(objeto.pais.lower())

def MostrarDatos(nombre,apellido,lista):
    print("")
    for i in lista:
        if i.nombre.lower() == nombre.lower() and i.apellido.lower() == apellido.lower():
            print("Nombre: " +  i.nombre)
            print("Apellido: " +  i.apellido)
            print("Edad:" + str(i.edad))
            print("Enfermedad: " + i.enfermedad)
            print("Pais de residencia: " + i.pais)
            if i.edad >= 60 :
                print("Condicion: " + i.condicion)
    print("")

def Buscar(nombre,apellido,lista):
    encontrado = False
    for i in lista:
        if i.nombre.lower() == nombre.lower() and i.apellido.lower() == apellido.lower():
            encontrado= True
            break
    return encontrado


def CalcularMayor(numUno,numDos,numTres,numCuatro):
    mayor = 0
    if numUno > numDos:
        mayor = numUno
    else:
        mayor = numDos

    if numTres >  mayor:
        mayor = numTres

    if numCuatro > mayor:
        mayor = numCuatro

    return mayor
        

def CambiarCaso(nombre,apellido,lista,listaDos):
    for i in lista:
        if i.nombre.lower() == nombre.lower() and i.apellido.lower() == apellido.lower():
            i.estatus = False
            i.enfermedad = ""
            listaDos.append(i)
            lista.remove(i)
            break

def pandemia(objeto,resfriado,covid,bronquitis,alergia,gripe):
    Menu()
    contador = 1
    cont = 0
    bron = 0
    res = 0
    co = 0
    gri = 0
    al =0
    while cont < 6:
        while True:
            sintoma = input("Sintoma " + str(contador) + ": " )
            if sintoma in resfriado or sintoma in covid or sintoma in gripe or sintoma in alergia or  sintoma in bronquitis or sintoma == "13":
                break
            else:
                print("Opcion no valida" + "\n")
        contador = contador + 1
        if sintoma == "13":
            break;
        else:
            if sintoma in resfriado:
                res = res + 1
            if sintoma in covid:
                co = co + 1
            if sintoma in gripe:
                gri = gri + 1
            if sintoma in alergia :
                al  = al + 1
            if sintoma in bronquitis:
                bron = bron + 1 
        cont = cont + 1

    print("")
    if co >= 3 :
        print("||| Tiene COVID-19 |||")
        objeto.estatus = True
        objeto.enfermedad = "COVID-19"
    elif res == 0 and gri == 0 and al == 0 and co ==0 and bron == 0 :
        print("||| Persona Sana |||")
        objeto.enfermedad = "Persona Sana"
    else:
        if CalcularMayor(res,gri,al,bron) == res:
            print("||| Tiene un Resfriado Común |||")
            objeto.enfermedad = " Resfriado Común"
        elif CalcularMayor(res,gri,al,bron) == al :
            print ("||| Presenta un Alergia |||")
            objeto.enfermedad = "Alergia"
        elif CalcularMayor(res,gri,al,bron) == gri:
            print("||| Preseta una Gripe |||")
            objeto.enfermedad = "Gripe"
        elif CalcularMayor(res,gri,al,bron) == bron:
            print("||| Presenta sintomas de bronquitis |||")
            objeto.enfermedad = "Sintomas de bronquitis"
    
        
        
        
    
    

activo = []
inactivo = []
fallecido=[]
recuperado = []
resfriado=[]
gripe = []
alergia = []
covid=[]
bronquitis = []
pais=[]

gripe.append("2")
gripe.append("9")
gripe.append("6")
gripe.append("10")

bronquitis.append("3")
bronquitis.append("4")
bronquitis.append("5")
bronquitis.append("6")

alergia.append("11")
alergia.append("2")
alergia.append("12")

resfriado.append("1")
resfriado.append("6")
resfriado.append("7")
resfriado.append("8")
resfriado.append("2")

covid.append("5")
covid.append("4")
covid.append("3")
covid.append("1")

opc = ""

while opc != "7":
    print("")
    print("1.Registrar un caso")
    print("2.Ver casos de un pais")
    print("3.Ver casos por edad")
    print("4.Ver casos por genero")
    print("5.Ver datos de un caso especifico")
    print("6.Cambiar estatus de un caso")
    print("7.Salir" + "\n")
    opc = input("OPC: ")
    print("")

    if opc == "1":
        while  True:
            print("")
            print("1.Niño")
            print("2.Adulto" )
            print("3.Mayor de edad" +  "\n")
            opc = input("OPC: ")
            print("")
            if opc == "1" or opc == "2" or opc == "3":
                break
            else:
                print("Opcion no valida" + "\n")
        if opc == "1":
            niño = Niños()
            niño.registrarNiños()
            paises(niño,pais)
            pandemia(niño,resfriado,covid,bronquitis,alergia,gripe)
            if niño.estatus == True:
                activo.append(niño)
            else:
                inactivo.append(niño)
        elif opc == "2":
            adulto = Adultos()
            adulto.registrarAdultos()
            paises(adulto,pais)
            pandemia(adulto,resfriado,covid,bronquitis,alergia,gripe)
            if adulto.estatus == True:
                activo.append(adulto)
            else:
                inactivo.append(adulto)
        elif opc == "3":
            anciano = Ancianos()
            anciano.registrarAncianos()
            paises(anciano,pais)
            pandemia(anciano,resfriado,covid,bronquitis,alergia,gripe)
            if anciano.estatus == True:
                activo.append(anciano)
            else:
                inactivo.append(anciano)

    elif opc == "2":
        print("")
        paisE = input("Pais a consultar: ")
        while paisE.isalpha() != True:
            print("Debe ingresar solo letras!" + "\n" )
            paisE = input("Pais a consultar: ")
        if not paisE.lower() in pais:
            print("No se han presentado casos en este pais..." + "\n")
        else:
            print("")
            print("-------ACTIVOS COVID-19-------")
            print("_______________________________")
            MostrarEspecifico(activo,paisE)

            print("-------INACTIVOS-------")
            print("_________________________")
            MostrarEspecifico(inactivo,paisE)

            print("-------FALLECIDOS-------")
            print("_________________________")
            MostrarEspecifico(fallecido,paisE)

            print("-------RECUPERADOS-------")
            print("__________________________")
            MostrarEspecifico(recuperado,paisE)


    elif opc == "3":
        while True:
            print("")
            print("1.Activos")
            print("2.Inactivos")
            print("3.Fallecidos")
            print("4.Recuperados" + "\n")
            opc = input("OPC: ")
            print("")
            if opc == "1" or opc == "2" or opc == "3" or opc =="4":
                break
            else:
                print("Opcion no valida" + "\n")
        
        if opc == "1" :
            print("-------ACTIVOS COVID-19--------")
            print("________________________________")
            MostrarNiños(activo)
            MostrarAdultos(activo)
            MostrarMayores(activo)
        elif opc == "2" :
            print("-------INACTIVOS-------")
            print("________________________" )
            MostrarNiños(inactivo)
            MostrarAdultos(inactivo)
            MostrarMayores(inactivo)
        elif opc == "3" :
            print("-------FALLECIDOS-------")
            print("_________________________")
            MostrarNiños(fallecido)
            MostrarAdultos(fallecido)
            MostrarMayores(fallecido)
        elif opc == "4":
            print("-------RECUPERADOS-------")
            print("__________________________")
            MostrarNiños(recuperado)
            MostrarAdultos(recuperado)
            MostrarMayores(recuperado)

    elif opc == "4":

        while True:
            print("")
            print("1.Activos")
            print("2.Inactivos")
            print("3.Fallecidos")
            print("4.Recuperados" + "\n")
            opc = input ("OPC: ")
            print("")
            if opc == "1" or opc == "2" or opc == "3" or opc == "4":
                break
            else:
                print("Opcion no valida" + "\n")

        if opc == "1" :
            print("-------ACTIVOS COVID-19--------")
            print("________________________________")
            MostrarHombres(activo)
            MostrarMujeres(activo)
        elif opc == "2" :
            print("-------INACTIVOS-------")
            print("________________________" )
            MostrarHombres(inactivo)
            MostrarMujeres(inactivo)
        elif opc == "3" :
            print("-------FALLECIDOS-------")
            print("_________________________")
            MostrarHombres(fallecido)
            MostrarMujeres(fallecido)
        elif opc == "4":
            print("-------RECUPERADOS-------")
            print("__________________________")
            MostrarHombres(recuperado)
            MostrarMujeres(recuperado)

    elif opc == "5":
        nombreC = input("Nombre del caso: ")
        while nombreC.isalpha() != True:
            print("Ingrese solo letras..." + "\n")
            nombreC = input("Nombre del caso: ")
            
        apellidoC = input("Apellido del caso: ")
        while apellidoC.isalpha() != True:
            print("Ingrese solo letras...")
            apellidoC = input("Apellido del caso: ")
        print("")
        if Buscar(nombreC,apellidoC,activo) == True:
            print("---ACTIVO COVID-19---")
            MostrarDatos(nombreC,apellidoC,activo)
        elif Buscar(nombreC,apellidoC,inactivo) == True :
            print("---INACTIVO---")
            MostrarDatos(nombreC,apellidoC,inactivo)
        elif Buscar(nombreC,apellidoC,recuperado) == True:
            print("---RECUPERADO---")
            MostrarDatos(nombreC,apellidoC,recuperado)
        elif Buscar(nombreC,apellidoC,fallecido) == True :
            print("---FAllECIDO---")
            MostrarDatos(nombreC,apellidoC,fallecido)
        else:
            print("Esta persona no esta registrada dentro del sistema...")
            
      

    elif opc == "6":
        nombreC = input("Nombre del caso: ")
        while nombreC.isalpha() != True:
            print("Ingrese solo letras..." + "\n")
            nombreC = input("Nombre del caso: ")

        apellidoC = input("Apellido del caso: ")
        while apellidoC.isalpha() != True:
            print("Ingrese solo letras...")
            apellidoC = input("Apellido del caso: ")

        if Buscar(nombreC,apellidoC,activo) == True:
            while True:
                print("")
                print("¿ A que estado desea cambiar ?" + "\n")
                print("1.Fallecido")
                print("2.Recuperado" + "\n")
                opc = input("OPC: ")
                if opc == "1" or opc == "2" :
                    break
                else:
                    print("Opcion no valida" + "\n")        
            if opc == "1":
                CambiarCaso(nombreC,apellidoC,activo,fallecido)
            elif opc == "2":
                CambiarCaso(nombreC,apellidoC,activo,recuperado)
                    
        else:
            print("Esta persona no tiene el virus..." + "\n")



            

       
  

