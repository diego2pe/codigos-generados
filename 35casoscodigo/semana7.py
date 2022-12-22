#semana 7
#estructuras secuenciales y selectiva

#caso1 programa para saber si aprobamos un curso

print("recuerde que la nota aprobatoria es 11")
nota1=float(input("ingrese su primera nota"))
nota2=float(input("ingrese su segunda nota"))
nota3=float(input("ingrese su tercera nota"))
nota4=float(input("ingrese su cuarta nota"))
promedio=(nota1+nota2+nota3+nota4)/4
if promedio>=11:
    print(F"Felicidades usted aprobo el curso con {promedio} de nota")
else:
    print("usted no aprobo el curso")

#caso2 programa para saber si un numero es negativo, positivo o cero
print("vamos a definir a un numero como positivo o negativo")
nume1=float(input("digite el numero a evaluar"))
if nume1>0:
    print("El numero",nume1,"es positivo")
elif nume1<0:
    print("El numero",nume1,"es negativo")
else :
    print("El numero",nume1,"no es negativo ni positivo")

#caso3 programa para saber si una nota es buena
print("bienvenido vamos a analizar si tu nota es\nbuena\nmuy buena\nmala")
not1=float(input("ingrese su nota obtenida"))
if not1>17 and not1<=20:
    print("usted alcanzo un muy buena nota")
elif not1>=14 and not1<=17:
    print("usted alcanzo una buena nota")
elif not1>=11 and not1<14:
    print("usted a obtenido una nota regular")
elif not1<=10:
    print("usted obtubo una mala nota")
else:
    print("ERROR las calificaciones esta en el rango de 1 a 20")

#caso4 progrma para saber si un niño resibira regaalo
var=int(input("¿Como se comporto el niño?\n1)bien\n2)mal"))
if var==1:
    print("el niño se porto bien por ende recibira su regalo")
elif var==2:
    print("el niño se ha portado mal por ende no tendra regalo")
else :
    print("ERROR ingrese una de las opciones proporcionada")

 #caso 5 programa de calculadora
print("bienvenido a calcufast")
num1=float(input("digite el primer numero"))
num2=float(input("digite el segundo numero"))
operacion=int(input("digite la operacion que desea realizar\n1)suma\n2)resta\n3)multipicacion\n4)division"))
if operacion==1:
    sum=num1+num2
    print("la suma es: ",sum)
elif operacion==2:
    rest=num1-num2
    print("la resta es: ",rest)
elif operacion==3:
     mult=num1*num2
     print("la multiplicacion es: ",mult)
elif operacion==4:
     div=num1/num2
     print("el resultado es:",div) 
else:
    print("ERROR")  
    
