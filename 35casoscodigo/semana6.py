#semana 6
#esctructuras selectiva
#caso 1
sexo=int(input("escriba su sexo:\n1) Femnino\n2) Masculino\n"))
if sexo== 2:
   print("usted es masculino")
elif sexo==1:
    print("usted es femenino")

#caso 2
edad=int(input("ingrese su edad correspondiente"))
if edad>=18:
    print("usted ya es mayor de edad")
else :
    print("usted aún no es mayor de edad")

#caso 3
despertar=int(input("¿a que hora te levantaste hoy?"))
if despertar<7:
    print("llegaras temprano a la universidad")
elif despertar>7:
    opcion1=int(input("¿como te transladaras a la universidad\n1)taxi\n2)combi"))
    if opcion1==1:
        print("llegaras temprano a la universidad")
    if opcion1==2:
        print("llegaras tarde a la universidad")

# caso 4
cuenta=int(input("bienvenido a bcp\ncontamos con tres tipos de cuentas las cuales son:\n1) cuenta a plazo fijo\n2) cuenta de ahorro\n3) cuenta sueldo\n"))
if cuenta==1:
    print("usted a elejido una cuenta a plazo fijo")
elif cuenta==2:
    print("usted a elejido una cuenta de ahorro")
elif cuenta==3:
    print("usted a elejido una cuenta sueldo")
else:
    print("ERROR digite un numero de las opciones mostradas")

#caso 5
region=int(input("seleccione que seccion del tipo de comida: \n1) Costa\n2) Sierra\n3) Selva\n"))
if region==1:
    print("el menu de la costa es: 1)ceviche\n2)lomo saltado\n3)causa")
if region==2:
    print("el menu de la sierra es: 1)pachamanca\n2)patasca\n3)cuy al horno")
if region==3:
    print("el menu de la selva es: 1)juanes\n2)tacacho con cecina\n3)chaufa amazonico")
