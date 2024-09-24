from inmueble import Inmueble
from casa import Casa
from departamento import Departamento 

class Inmobiliaria():
    
    def __init__(self) -> None:
        self.inmuebles = {}

    def agregar_inmueble(self, valores):
        datos = valores.split(",")
        if datos[0] == "1":
            nuevo = Casa.cargar_datos(datos)
        elif datos[0] == "2":
            nuevo = Departamento.cargar_datos(datos)
                
        self.inmuebles[nuevo.codigo] = nuevo
        
    def suma_alq(self):
        return sum(map(lambda i: i.alquiler, self.inmuebles.values()))
    
    def casa_premium(self):
        cant = 0
        for i in self.inmuebles.values():
            if i.tipo == 1 and i.premium:
                cant += 1
                
        return cant
    
    def menor_alquiler(self):
        propietario = ""
        menor = 1000000000000000000000
        for i in self.inmuebles.values():
            if i.tipo == 2 and i.alquiler < menor:
                menor = i.alquiler
                propietario = i.propietario
        return propietario
    
    