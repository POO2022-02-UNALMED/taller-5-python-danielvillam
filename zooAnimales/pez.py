from zooAnimales.animal import Animal

class Pez (Animal):
    
    salmones=0
    bacalaos=0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas=cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas

    @ classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @ classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones+=1
        pez = Pez(nombre, edad, "oceano", genero, "rojo",6)
        cls._listado.append(pez)
        return pez

    @ classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.bacalaos+=1
        pez = Pez(nombre, edad, "oceano", genero, "gris",6)
        cls._listado.append(pez)
        return pez

    def movimiento():
        return "nadar"
