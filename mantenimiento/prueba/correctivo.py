from mantenimiento import Mantenimiento

class Correctivo(Mantenimiento):
    def __init__(self, operario, fecha, importeRepuestos, horas, importeTecnico):
        super().__init__(operario, fecha, importeRepuestos)
        self._horas = horas
        self._importeTecnico = importeTecnico

    @property
    def horas(self):
        return self._horas
    @property
    def importeTecnico(self):
        return self._importeTecnico
    
    def gastos(self):
        return super().gastos() + self.importeTecnico