# Defineix una jerarquia de figures amb les classes Figura, Cercle, Triangle, Rectangle i Quadrat.
# La clase Figura tindrá dos métodes abstractes area i perimetre, que implementarán la resta
# de classes. La classe figura serà el que s'anomena una interfície informal, ja que tots els
# seus mètodes són abstractes. Per a definir que són abstractes, simplement utilitzeu la
# instrucció pass al bloc de la funció.

# El Cercle rebrá el radi com a argument al seu constructor, el Triangle el costat i el Rectangle la base i l'altura.
#Cercle, Triangle i Rectangle heredarán de Figura directament.
#Quadrat heredará de Rectangle, però al constructor sols rebrá un argument, el costat.
#Crea un objecte de cada tipus i imprimeix les seues característiques.

import math



class Figura:
    
    #abstracto pones pass
    def area(self) -> int:
        pass
    def perimetre(self) -> int:
        pass
class Cercle(Figura):
    #Constructor Cercle
    def __init__(self,radi):
        self.radi=radi
    def area(self) -> int:
        return int(math.pi*self.radi)
    def perimetre(self) -> int:
        return int(self.radi*2*(math.pi)) 
        

class Triangle(Figura):
    def __init__(self,costat):
        self.costat=costat
    def area(self):
        altura=(math.sqrt(3) * self.costat) / 2 
        return int(self.costat*altura/2)
    def perimetre(self):
        return int(self.costat*3)

class Rectangle(Figura):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return int(self.base*self.altura)
    def perimetre(self):
        base2=self.base*2
        altura2=self.altura*2
        return int(base2+altura2)

class Quadrat(Rectangle):
    def __init__(self,costat):
        self.costat=costat
    def area(self):
        return self.costat*2
    def perimetre(self):
        return self.costat*4

triangle=Triangle(5)
print("Dades del Triangle Costat:"+str(triangle.costat)+" Perimetre:"+str(triangle.perimetre())+" Area:"+str(triangle.area())+" Altura: "+str((int(math.sqrt(3) * triangle.costat) / 2)))
rectangle=Rectangle(15,5)
print("Dades del Rectangle Base:"+str(rectangle.base)+" Altura:"+str(rectangle.altura)+" Perimetre:"+str(rectangle.perimetre())+" Area:"+str(rectangle.area()))
quadrat=Quadrat(5)
print("Dades del Quadrat Costat:"+str(quadrat.costat)+" Perimetre:"+str(quadrat.perimetre())+" Area:"+str(quadrat.area()))
cercle=Cercle(10)
print("Dades del Quadrat Radi:"+str(cercle.radi)+" Perimetre:"+str(cercle.perimetre())+" Area:"+str(cercle.area()))






