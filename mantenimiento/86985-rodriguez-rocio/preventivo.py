from mantenimiento import Mantenimiento

"""Si es un preventivo, resultado del mantenimiento (1, 2 o 3)
1 si la máquina se encuentra funcionando correctamente, 
2 si se recomienda una revisión del servicio técnico del fabricante y 
3 si se detecta alguna rotura.
   Si es un preventivo, importe de los insumos; """

class Preventivo(Mantenimiento):
    def __init__(self, fecha, operario, importe_repuestos, resultado, imp_insumos):
        super().__init__(fecha, operario, importe_repuestos)
        self._resultado = resultado
        self._imp_insumos = imp_insumos
        
    @property
    def imp_insumos(self):
        return self._imp_insumos
    
    @property
    def resultado(self):
        return self._resultado
    
    def gastos(self):
        return super().gastos() + self.imp_insumos