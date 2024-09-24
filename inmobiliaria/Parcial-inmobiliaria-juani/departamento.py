from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codigo, propietario, superficie, importe, expensas, piso) -> None:
        super().__init__(codigo, propietario, superficie, importe)
        self.expensas = expensas
        self.piso = piso
    
    @staticmethod
    def cargar_datos(datos):
        #datos = valores.split(",")
        codigo = int(datos[1])
        propietario = datos[2]
        importe = float(datos[3])
        superficie = float(datos[4])
        expensas = float(datos[5])
        piso = int(datos[6])
        return Departamento(codigo, propietario, superficie, importe, expensas, piso)
    
    @property
    def alquiler(self):
        alq = self.importe_base + self.expensas
        if self.piso < 3:
            alq += 20000
        return alq
    
    @property
    def tipo(self):
        return 2
        
    
    
    
    