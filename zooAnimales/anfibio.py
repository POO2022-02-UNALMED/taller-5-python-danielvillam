from zooAnimales.animal import Animal

class Anfibio (Animal):
    
    ranas=0
    salamandras=0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel=colorPiel

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso=venenoso

    @ classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @ classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas+=1
        anfibio = Anfibio(nombre, edad, "selva", genero, "rojo",True)
        return anfibio

    @ classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras+=1
        anfibio = Anfibio(nombre, edad, "selva", genero, "negro y amarillo",False)
        return anfibio

    def movimiento():
        return "saltar"
