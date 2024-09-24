from inmueble import Inmueble

class Casa(Inmueble):
    def __init__(self, codigo, propietario, superficie, importe, habitaciones, pileta) -> None:
        super().__init__(codigo, propietario, superficie, importe)
        self.habitaciones = habitaciones
        self.pileta = pileta
        
    @staticmethod
    def cargar_datos(datos):
        #datos = valores.split(",")
        codigo = int(datos[1])
        propietario = datos[2]
        importe = float(datos[3])
        superficie = float(datos[4])
        habitaciones = int(datos[5])
        pileta = int(datos[6])
        return Casa(codigo, propietario, superficie, importe, habitaciones, pileta)
    
    @property
    def tipo(self):
        return 1
    
    @property
    def alquiler(self):
        alq = self.importe_base + (30000 * self.habitaciones)
        if self.pileta == 1:
            alq += 100000
        return alq
        
    @property
    def premium(self):
        if self.superficie > 150 and self.habitaciones > 2 and self.pileta == 1:
            return True
        return False
        
            
    