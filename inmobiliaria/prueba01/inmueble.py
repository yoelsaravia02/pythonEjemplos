class Inmueble():
    def __init__(self, codNumerico, propietario, superficie, impBaseAlquiler):
        self._codNumerico = codNumerico
        self._propietario = propietario
        self._superficie = superficie
        self._impBaseAlquiler = impBaseAlquiler

    @property
    def codNumerico(self):
        return self._codNumerico
    @property
    def propietario(self):
        return self._propietario
    @property
    def superficie(self):
        return self._superficie
    @property
    def impBaseAlquiler(self):
        return self._impBaseAlquiler
    
    def impTotal(self):
        return self._impBaseAlquiler