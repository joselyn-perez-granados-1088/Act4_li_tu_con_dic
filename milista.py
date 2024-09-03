#uso de listas ejemplo
MisNovios= ["jonathan ♥","jona ♥","mamahuevo ♥"]
MisLugares= [1,2,3]
print(MisNovios)
print(MisLugares)
print("----accediendo a los elementos de la lista----")
print(MisNovios[-3])
if "jonathan" in MisNovios:
    print("si, esta en la lista de mis novios")
else:
    print("no esta en la lista de novios")
print ("Numeros de novias")
Novias=len(MisNovios)
print(f"Numero de novios: {Novias}")
print("Ciclo en listas")
posicion=1
for medianaranja in MisNovios:
    print(posicion ,"   ", medianaranja)
    posicion=posicion+1



