from correctivo import Correctivo

class Maquina():
    def __init__(self):
        self._mantenimientos = []

    def agregarMantenimiento(self, mantenimiento):
        self._mantenimientos.append(mantenimiento)

    def sumaGastos(self):
        suma = 0
        for mant in self._mantenimientos:
            suma += mant.gastos()
        return suma
    
    def cantCaros(self):
        cant = 0
        for mant in self._mantenimientos:
            if mant.gastos() > 10000:
                cant += 1
        return cant
    
    def roturaMasLarga(self):
        fecha = []
        operario = []
        horas = 0
        for mant in self._mantenimientos:
            if isinstance(mant, Correctivo) and mant.horas > horas:
                horas = mant.horas
        for mant in self._mantenimientos:
            if isinstance(mant, Correctivo) and mant.horas == horas:
                fecha.append(mant.fecha)
                operario.append(mant.operario)

        return fecha, operario, horas