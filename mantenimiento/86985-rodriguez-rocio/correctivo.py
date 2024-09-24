from mantenimiento import Mantenimiento

"""si es un correctivo, cantidad de horas de parada.
6. si es un correctivo, importe que cobró el técnico."""
class Correctivo(Mantenimiento):
    def __init__(self, fecha, operario, importe_repuestos, horas,imp_tecnico):
        super().__init__(fecha, operario, importe_repuestos)
        self._horas_parada = horas
        self._imp_tecnico = imp_tecnico
        
    @property
    def imp_tecnico(self):
        return self._imp_tecnico
    
    @property
    def horas(self):
        return self._horas_parada
    
    def gastos(self):
        return super().gastos() + self.imp_tecnico