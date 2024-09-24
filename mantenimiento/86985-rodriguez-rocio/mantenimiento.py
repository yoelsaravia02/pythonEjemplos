
class Mantenimiento():
    def __init__(self, fecha, operario, importe_repuestos):
        self._fecha = fecha
        self._operario = operario
        self._importe_repuestos = importe_repuestos
    
    
    @property
    def fecha(self):
        return self._fecha
    
    @property
    def operario(self):
        return self._operario
    
    
    @property
    def importe_repuestos(self):
        return self._importe_repuestos
    

    def gastos(self):
        return self._importe_repuestos
    