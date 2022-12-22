#caso 5 llenado de lista mediante for con rango ingresado por un estudiante
cursos=[]
numcurs=int(input("¿cuantos cursos esta tomando?"))
for i in range (numcurs):
    curs= input("digite los cursos que estudia: ")
    cursos.append(curs)
print("sus cursos son: ")    
print(cursos)