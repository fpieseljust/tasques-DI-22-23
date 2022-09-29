#Crea una aplicació que vaja llegint 
# operacions d'un fitxer (una operació per línia) i 
# afegisca els resultats. Per exemple, si llig: 4 + 4
#Haurà de generar: 4 + 4 = 8
#Utilitza funcions anònimes per a implementar les operacions.

from __future__ import division
from tkinter import Y


with open('operacions.txt', 'r') as r:
    with open('resultats.txt', 'w') as w:
        suma=lambda x,y: x+y
        resta=lambda x,y: x-y
        mult=lambda x,y: x*y
        div=lambda x,y: x+y
        for linea in r.readlines():
            res=''
            #.split borras los espacios
            lista=linea.split()
            op=lista[1]
            lista.pop(1)
            # Transformamos los valores de la lista en enteros
            lnum=list(map(int, lista))
            match op:
                case '+':
                     res=str(suma(lnum[0],lnum[1]))
                case '-':
                    res=str(resta(lnum[0],lnum[1]))
                case '*':
                    res=str(mult(lnum[0],lnum[1]))
                
                case '/':
                    res=str(div(lnum[0],lnum[1]))

                case _:
                    print("Operador no valido")
            

            tres=str(lnum[0])+' '+op+' '+str(lnum[1])+' = '+res+'\n'
            w.write(tres)



    