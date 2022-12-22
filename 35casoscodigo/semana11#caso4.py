
#caso 4 programa para saber el valor del factorial de un numero
while True:
    num4=int(input("ingrese el numero de que se quiere hallar su factorial\n"))
    fact=1
    i=1
    while i<=num4:
        fact*=i
        i+=1
    print(F"el factorial del numero{num4} es:",fact)