import csv

from maquina import Maquina
from preventivo import Preventivo
from correctivo import Correctivo

maq = Maquina()

with open("mantenimientos.csv", "r") as arch:
    lector = csv.reader(arch)

    for linea in lector:
        tipo, fecha, operario, importeRepuestos, dato1, dato2 = linea
        if tipo == "1":
            mant = Preventivo(fecha, operario, float(importeRepuestos), dato1, float(dato2))
        elif tipo == "2":
            mant = Correctivo(fecha, operario, float(importeRepuestos), int(dato1), float(dato2))
        
        maq.agregarMantenimiento(mant)