from correctivo import Correctivo

class Maquina():
    def __init__(self):
        self._mantenimientos = []
        
    def cantidad_mant(self):
        return len(self._mantenimientos)
    
    def nuevo_mantenimiento(self, mantenimiento):
        self._mantenimientos.append(mantenimiento)
        
    def suma_gastos_mantenim(self):
        suma = 0
        for mant in self._mantenimientos:
            suma += mant.gastos()
        return suma
    
    def mantenim_caros(self):
        cantidad = 0
        for mant in self._mantenimientos:
            if mant.gastos() > 10000:
                cantidad += 1
        return cantidad

    def rot_mas_larga(self):
        fecha= []
        operario = []
        horas = 0
        for mant in self._mantenimientos:
            if isinstance(mant,Correctivo) and mant.horas > horas:
                horas = mant.horas
        for mant in self._mantenimientos:
            if isinstance(mant,Correctivo) and mant.horas == horas:
                fecha.append(mant.fecha)
                operario.append(mant.operario)
                
        return fecha, operario , horas 