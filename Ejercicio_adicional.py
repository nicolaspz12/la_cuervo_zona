name= input("Ingresa el nombre del estudiante: ")
# (name) ingresa y almacena el nombre del estudiante
notestudent = float(input("Ingresa la calificación promedio de actividades en clase (30%): "))
#(notestudent) almacena el promedio de actividades
projectnote = float(input("Ingresa la calificación del proyecto final (50%): "))
#(projectnot) almacena la calificacio del proyecto
testnote = float(input("Ingresa la calificación promedio de evaluaciones parciales (20%): "))
# (testnote) almacena las calificaciones de las evaluaciones
finalnote = (notestudent * 0.3) + (projectnote * 0.5) + (testnote * 0.2) 
#(finalnote) contiene la formula para obtener el resultado
print("La nota final de algoritmia del estudiante", name, "es:", finalnote)
# imprime el resultado segun lo pedido en la guia