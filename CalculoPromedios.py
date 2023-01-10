
Practica1= (float(input("Nota de la Practica 1: ")))
Practica2= (float(input("Nota de la Practica 2: ")))
Practica3= (float(input("Nota de la Practica 3: ")))
ExamenPromedio= (float(input("Nota del primer examen parcial: ")))
ExamenPromedio2= (float(input("Nota del segundo examen parcial: ")))
ExamenFinal= (float(input("Nota del examen final:")))

PromedioPractica = (Practica1+Practica2+Practica3) / 3
PromedioFinal = (PromedioPractica+ExamenPromedio+ExamenPromedio2+3*ExamenFinal) / 6

print("El promedio de practica del estudiante es de:\n ",
PromedioPractica," \n Y el promedio final del estudiante es de:\n ", PromedioFinal)

