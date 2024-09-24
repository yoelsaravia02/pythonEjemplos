from mantenimiento import Mantenimiento

class Preventivo(Mantenimiento):
    def __init__(self, operario, fecha, importeRepuestos, importeInsumos, resultado):
        super().__init__(operario, fecha, importeRepuestos)
        self._importeInsumos = importeInsumos
        self._resultado = resultado
    @property
    def importeInsumos(self):
        return self._importeInsumos
    @property
    def resultado(self):
        return self._resultado 
    
    def gastos(self):
        return super().gastos() + self.importeInsumos