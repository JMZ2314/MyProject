class estudiar():

    def __init__(self):
        self.materias=0
        self.horas=0
        self.lista=[]
        self.registrado= False

    

    def EstaIncluida(self,materia,lista=[]):
        for i in lista :
            if materia == i :
                logico=True
                break
            else:
                logico=False
        return logico



    def Repetido(self,materia,lista=[]):
        return materia in lista
        


    def HorasLimite(self,horas):
        if horas < 3 :
            print("Solo se acepta un minimo de 3 horas")
            print("")
            return  False
        elif horas > 6 :
            print("Solo se acepta un maximo de 6 horas")
            print("")
            return False
        else :
            print("Numero de horas incrito")
            print("")
            return True

    def MateriasLimite(self,materias) :
        if materias < 4 :
            print("Solo se acepta un minimo de 4 materias por dia")
            print("")
            return False
        elif materias > 8 :
            print("Solo se acepta un maximo de 5 materias por dia")
            print("")
            return False
        else :
            print("Numeros de materias inscrito")
            print("")
            return True




estudiante = estudiar()
materias=[]
MateriasInscritas = []

materias.append("literatura")
materias.append("biologia")
materias.append("matematica")
materias.append("fisica")
materias.append("historia")
materias.append("arte")
materias.append("programacion")
materias.append("estructura de datos")

print("CONTROL DE ESTUDIO")
print("___________________")
print("")
print("Las materias disponibles en el sistema son : ")
print("")
print(materias)
print("")

numero_horas =int(input("Horas a estudiar: "))

while estudiante.HorasLimite(numero_horas) != True :
    numero_horas=int(input("Horas a Estudiar: "))

numero_materias =int(input("Numero de materias: "))

while estudiante.MateriasLimite(numero_materias) != True :
    numero_materias=int(input("Numero de materias: "))


contador=0

while contador < numero_materias:
    asig=input("Materia: ")
    
    if estudiante.EstaIncluida(asig,materias) == True:
        if estudiante.Repetido(asig,MateriasInscritas) == True:
            print("Esta materia ya esta inscrita")
            print("")
            contador =contador -1
        else:
            MateriasInscritas.append(asig)
    else:
        print("Esta materia no esta dentro del programa")
        print("")
        contador = contador -1
    contador = contador + 1
    print("")

estudiante.lista=MateriasInscritas
estudiante.horas=numero_horas
estudiante.materias=numero_materias
estudiante.registrado=True

print("Datos del estudiante")
print("____________________")
print("")
print("Horas: " ,estudiante.horas)
print("Materias: ",estudiante.materias)
print("Materias  inscritas: ", estudiante.lista )
print("Estado: ",estudiante.registrado )
print("")
print("---REGISTRO FINALIZADO---")
     
    

                
        
   
        
         


    
        
