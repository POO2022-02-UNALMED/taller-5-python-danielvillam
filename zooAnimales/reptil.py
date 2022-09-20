from zooAnimales.animal import Animal

class Reptil (Animal):
    
    iguanas=0
    serpientes=0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola=largoCola

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas

    @ classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @ classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas+=1
        reptil = Reptil(nombre, edad, "humedal", genero, "verde",3)
        return reptil

    @ classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes+=1
        reptil = Reptil(nombre, edad, "jungla", genero, "blanco",1)
        return reptil

    def movimiento():
        return "reptar"
