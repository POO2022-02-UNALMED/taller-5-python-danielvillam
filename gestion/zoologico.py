class Zoologico:
    
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas=[]

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre=nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion

    def agregarZonas(self, zona):
        zona.setZoo(self)
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        cantTot=0
        for i in self._zonas:
            cantTot+=i.cantidadAnimales()
        return cantTot

    def getZona(self):
        return self._zonas
