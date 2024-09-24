class Mantenimiento():
    def __init__(self, operario, fecha, importeRepuestos):
        self._operario = operario
        self._fecha = fecha
        self._importeRepuestos = importeRepuestos
    
    @property
    def operario(self):
        return self._operario
    @property
    def fecha(self):
        return self._fecha
    @property
    def importeRepuestos(self):
        return self._importeRepuestos
    
    def gastos(self):
        return self._importeRepuestos