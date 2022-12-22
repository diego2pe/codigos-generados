#caso 3 programa para hallar el promedio de edades

while True:
    num3=int(input("ingrese la cantidad de edades a procesar\n"))
    suma=0
    i=1
    while i<=num3:
        numero=int(input(F"digite el numero{i}\n"))
        suma+=numero
        i+=1
        prom=suma/num3 
    print("el promedio de edades es: ",prom)  
