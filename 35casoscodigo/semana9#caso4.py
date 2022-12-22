#caso 4 llenado de una lista mediante for con rango establecido
numerit=[]
i=0
for i in range (3):
    elem = input(F"digite numero {i+1}: ")
    numerit.append(elem)

print(numerit)