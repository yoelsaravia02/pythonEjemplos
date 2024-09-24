import csv

from inmobiliaria import Inmobiliaria
from casa import Casa
from departamento import Departamento

inmobiliaria = Inmobiliaria()

with open("inmuebles.csv", "r") as arch:
    lector = csv.reader(arch)

    for linea in lector:
        tipo, cod, propietario, alqBase, superficie, dato1, dato2 = linea
        if tipo == "1":
            inm = Casa(cod, propietario, int(superficie), alqBase, int(dato1), dato2)
        if tipo == "2":
            inm = Departamento(cod, propietario, int(superficie), alqBase, float(dato1), int(dato2))
        
        inmobiliaria.nuevoInmueble(inm)

print("RESULTADOOSSSSSSS")
print("1- Suma de alquileres: $", inmobiliaria.sumaAlquileres())
print("2- Cantidad de casas caras: ", inmobiliaria.cantCasasPremium())