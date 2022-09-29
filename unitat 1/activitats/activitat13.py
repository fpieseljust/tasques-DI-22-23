

from random import randint

import random
class numeroBajo(Exception):
    pass

class numeroGrande(Exception):
    pass



aleatorio=randint(0,100)
num=-1
while aleatorio!=num:
    try:    
        num=int(input("Dime un numero: "))
         #Constrolamos el error y lanzamos con raise el error personalizado que lo controlara el except
         
        if num<aleatorio:
            raise numeroBajo()
        else:
            raise numeroGrande()
    except numeroBajo:
        print("El numero introducido es mas bajo")
    except numeroGrande:
        print("El numero introducido es mas alto")
    except ValueError:
        print("No has introducido un numero entero")


print("Has adivinado el numero")



    

