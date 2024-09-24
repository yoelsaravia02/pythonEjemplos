class Inmueble():
    def __init__(self, codigo, propietario, superficie, importe) -> None:
        self.codigo = codigo
        self.propietario = propietario
        self.superficie = superficie
        self.importe_base = importe
        
    def cargar_datos(self, datos):
        pass
    
    @property
    def alquiler(self):
        pass
    
    @property
    def tipo(self):
        pass
    
    @property
    def premium(self):
        pass

    