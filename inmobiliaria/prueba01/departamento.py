from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codNumerico, propietario, superficie, impBaseAlquiler, numPiso, expensas):
        super().__init__(codNumerico, 
        propietario, superficie, impBaseAlquiler)
        self._numPiso = numPiso
        self._expensas = expensas

    @property
    def numPiso(self):
        return self._numPiso
    @property
    def expensas(self):
        return self._expensas
    
    def impTotal(self):
        if self._numPiso < 3:
            return float(super().impTotal()) + 20000 + self._expensas
        return float(super().impTotal()) + self._expensas