import math
#semana 5
#estructuras secuenciales

#caso 1 programa que pregunte nombre, consulta y salude.
print("Bienvenido a consultora Perez")
nombre=input("ingese su nombre completo")
razon=input("¿Cual es su consulta?")
print("Hola",nombre,"su consulta",razon,"se ha registrado con éxito")

#caso 2 programa para hallar area de triangulo
print("Bienvenido a calcuArea")
base=float(input("ingese la longitud de la base "))
altura=float(input("ingrese la longitud de la altura"))
Area= (base*altura)/2
print("Hola el area del triangulo solicitado es: ",Area)
#caso 3 programa para hallar la longitud de la hipotenusa de un triangulo rectangulo
print("Bienvenido a Geoisi")
cateto1=float(input("ingese la longitud de un cateto"))
cateto2=float(input("ingrese la longitud del otro cateto"))
suma= (cateto1**2)+(cateto2**2)
hipotenusa=math.sqrt(suma)
print("Hola la hipotenusa del triangulo solicitado es: ",hipotenusa)
#caso 4 programa para transformar minutos a horas y minutos
print("Bienvenido a calcuHoras")
minutos=float(input("ingrese el numero total de minutos a transformar"))
horas=minutos/60
min=minutos%60
print("Hola los ",minutos,"minutos equivale a ",horas,"horas con",min,"minutos")

#caso 5 programa para calcular el perimetro de un rectangulo
lado=float(input("ingrese la longitud del lado"))
altura=float(input("ingrese la longitud de la altura"))
perimetro=2*(lado+altura)
print("el perimetro del rectangulo es: ",perimetro)





