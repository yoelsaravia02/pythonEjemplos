from casa import Casa
from departamento import Departamento

class Inmobiliaria():
    def __init__(self):
        self._inmuebles = []
    
    def nuevoInmueble(self, inmueble):
        self._inmuebles.append(inmueble)

    def sumaAlquileres(self):
        suma = 0
        for inm in self._inmuebles:
            suma += inm.impTotal()
        return suma

    def cantCasasPremium(self):
        cant = 0
        for inm in self._inmuebles:
            if isinstance(inm, Casa) and inm.superficie > 150 and inm.cantDormitorios > 2 and inm.pileta == "1":
                cant += 1
        return cant
    
    def propAlqMasBajo(self):
        propietario = ""
        menor = self._inmuebles[0].impTotal()
        for inm in self._inmuebles:
            if isinstance(inm, Departamento) and inm.impTotal() < menor:
                menor = inm.impTotal()
                propietario = inm.propietario
        return menor, propietario
                