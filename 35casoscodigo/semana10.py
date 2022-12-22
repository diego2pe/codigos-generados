#semana 10
import math
#caso 1 conteo de numeros pares e impares de una lista de numeros ingresados
cant1=int(input("¿cuantos numeros son los que va a digitar?\n"))
contP=0
contI=0
for i  in range (cant1):
   num1=int(input(F"digite el numero {i+1}\n"))
   if num1%2==0:
      contP+=1
   else :
      contI+=1
print("la cantidad de numeros pares son: ",contP)
print("la cantidad de numeros impares es: ",contI)
#caso 2 programa para hallar la suma de numeros pares e impares de una lista ingresada por el cliente
cant2=int(input("¿cuantos numeros va a ingresar?\n"))
acumI=0
acumP=0
for i in range (cant2):
    num2=int(input(F"digite el numero{i+1}\n"))
    if num2%2==0:
       acumP+=num2 
    else:
      acumI+=num2

print("la suma de los numeros pares es :",acumP)
print("la suma de los numeros impares es :",acumI)


#caso 3 programa para reconocer dentro de los primeros numeros naturales la suma de numeros impares y cuantos numeros son pares
cant=int(input("¿cuantos numeros va a analizar?\n"))
conta=0
acum=0
for i in range (cant):
    num=int(input(F"digite el numero{i+1}\n"))
    if num%2==0:
       conta+=1
    else:
      acum+=num

print("la cantidad de numeros pares son: ",conta)
print("la suma de numeros impares es: ",acum)
#caso 4 programa para hallar la multipliacion de una lista ingresada por el usuario

cant4=int(input("¿cuantos numeros va a incertar?"))
acumM=1
for i in range (cant4):
   num4=int(input(F"digite el numero{i+1}\n"))
   if num4 !=0:
      acumM*=num4
   else:
      acumM==0
print("la multiplicacion de los numeros :",acumM)      
#caso 5 programa para calcular la suma de los cuadrados de los numeros ingresados por el usuario
cant5=int(input("¿cuantos numeros va a digitar?\n"))
acum5=0
for i in range(cant5):
   num5=int(input(F"digite el numero{i+1}\n"))
   acum5+=num5**2
print("la suma de los cuadrados de los numeros ingressados es:",acum5)   