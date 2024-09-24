from inmueble import Inmueble

class Casa(Inmueble):
    def __init__(self, codNumerico, propietario, superficie, impBaseAlquiler, cantDormitorios, pileta):
        super().__init__(codNumerico, propietario, superficie, impBaseAlquiler)
        self._cantDormitorios = cantDormitorios
        self._pileta = pileta
    @property
    def cantDormitorios(self):
        return self._cantDormitorios
    @property
    def pileta(self):
        return self._pileta
    
    def impTotal(self):
        return float(super().impTotal()) + (30000 * self._cantDormitorios) + (100000 * int(self._pileta))
    