# Jhonmaiker Zerpa

promedio=0
aprobados=0
reprobados=0
notas=0
porcentaje=0
temporal=0
Mayor=0
Menor=20
acumulador=0
contador=1

while True :
    try:
        porcentaje=int(input("Ingrese el porcentaje de la evaluacion: "))
        if porcentaje >= 5 and porcentaje <= 40 :
            break
        else:
            print("Se acepta un rango entre 5 y 40 " + "\n")
    except:
        print("Ingrese solo numeros" + "\n")


NotasAlumnos=[]
PorcentajesNotas=[]
print("")

for i in range(1,11):

    while True :
        try:
            notas=int(input("Nota: " + str(i) + ": "))
            if notas >=0 and notas <=20:
                break
            else:
                print("Se acepta un rango entre 0 y 20" + "\n")
        except:
            print("Solo puede ingresar numeros" + "\n")

    if notas >= 10 :
        aprobados =aprobados + 1
    else:
        reprobados = reprobados + 1

    NotasAlumnos.append(notas)

for j in NotasAlumnos:
    if j < Menor :
        Menor=j

    if j > Mayor:
        Mayor=j

    temporal=(j*porcentaje)/100 

    PorcentajesNotas.append(temporal)
    acumulador=acumulador + j;



promedio=acumulador/5

print("")
print("PORCENTAJE POR NOTAS ")
print("______________________")
print("")

for i in PorcentajesNotas:
    print("Nota ", contador, ": ",i)
    contador=contador +1

print()
print("El promedio de la seccion es : ", promedio)
print("El numero de aprobados es: ", aprobados)
print("El numero de reprobados es: ",reprobados)
print("La mayor nota fue: ", Mayor)
print("La menor nota fue: ", Menor)



    


             
    
        
