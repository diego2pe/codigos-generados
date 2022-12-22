#caso 5 programa para pedir un numero positivo

numero=int(input("escriba un  numero positivo:\n"))
while numero<0:
    print("!USTED A DIGITADO UN NUMERO NEGATIVO¡ INTENTELO DE NUEVO")
    numero=int(input("Escriba un numero positivo:\n"))
print("gracias por su colaboracion")