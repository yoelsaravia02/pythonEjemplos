from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codNumerico, propietario, superficie, impBaseAlquiler, expensas, numPiso):
        super().__init__(codNumerico, propietario, superficie, impBaseAlquiler)
        self._expensas = expensas
        self._numPiso = numPiso

    @property
    def expensas(self):
        return self._expensas
    @property
    def numPiso(self):
        return self._numPiso
    
    def impDefinitivo(self):
        if self._numPiso < 3:
            return super().impDefinitivo() + 20000 + self._expensas
            
    