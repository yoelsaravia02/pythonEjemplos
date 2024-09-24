from departamento import Departamento
from casa import Casa

class Inmobiliaria():
    def __init__(self):
        self._inmuebles = []

    def agregarInmueble(self, inmueble):
        self._inmuebles.append(inmueble)
    
    def sumaAlquileres(self):
        suma = 0
        for inmueble in self._inmuebles:
            suma += inmueble.impBaseAlquiler
        return suma
    
    def cantCasasPremium(self):
        cant = 0
        for inmueble in self._inmuebles:
            if isinstance(inmueble, Casa) and inmueble.superficie > 150 and 

    def propAlqMasBajo(self):
        alqMasBajo = self._inmuebles[0].impBaseAlquiler
        for inmueble in self._inmuebles:
            if isinstance(inmueble, Departamento) and inmueble.impBaseAlquiler < alqMasBajo:
                alqMasBajo = inmueble.impBaseAlquiler
        return alqMasBajo