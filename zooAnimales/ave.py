from zooAnimales.animal import Animal

class Ave (Animal):
    
    halcones=0
    aguilas=0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas=colorPlumas

    @ classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @ classmethod
    def crearHalcones(cls, nombre, edad, genero):
        cls.halcones+=1
        ave = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls._listado.append(ave)
        return ave

    @ classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas+=1
        ave = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls._listado.append(ave)
        return ave

    def movimiento():
        return "volar"
