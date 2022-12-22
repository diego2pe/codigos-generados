#caso 2 juego de suerte de numeros sea 4 el numero ganador dentro del rango[1;10]
while True:
 num2=int(input("ingrese su numero de la suerte comprendido ente 1 y 10\n"))
 while num2>0 and num2<11:
        if num2==4:
            print("felicidades usted a ganado el juego")
            break
        elif num2>10 or num2<1:
            print("ERROR digite un numero dentro del rango [1,10]")
            break
        else:
            print("sigue intentando")
            break