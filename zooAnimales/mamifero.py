from zooAnimales.animal import Animal

class Mamifero (Animal):
    
    caballos=0
    leones=0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje=pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self,patas):
        self._patas=patas

    @ classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @ classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos+=1
        mamifero = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls._listado.append(mamifero)
        return mamifero

    @ classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones+=1
        mamifero = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls._listado.append(mamifero)
        return mamifero