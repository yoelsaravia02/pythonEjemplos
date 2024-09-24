import csv
from maquina import Maquina
from preventivo import Preventivo
from correctivo import Correctivo

"""
El archivo posee la siguiente estructura:
1. Tipo de mantenimiento: 1 para preventivo y 2 para correctivo
2. Fecha: una cadena
3. Operario: nombre del operario que realizó el mantenimiento
4. Importe de repuestos: número de tipo float
5. Si es un preventivo, resultado del mantenimiento (1, 2 o 3); si es un correctivo, cantidad de horas de parada.
6. Si es un preventivo, importe de los insumos; si es un correctivo, importe que cobró el técnico.
"""
"""
REPORTE
1- Suma de gastos: que informe el total abonado por todo concepto en todos los mantenimientos 
registrados.
2- Cantidad de mantenimientos caros: que informe el total de mantenimientos de cualquier tipo
que hayan tenido un gasto total de más de $10.000
3- Rotura más larga: que informe la fecha y el nombre del operario del mantenimiento correctivo 
de mayor duración.
"""
maq = Maquina()

archivo = open("mantenimientos.csv","r")
lector = csv.reader(archivo)

for linea in lector:
    tipo , fecha , operario , importe_repuestos, dato_1 , dato_2 = linea
    if tipo == "1":
        mantenim = Preventivo(fecha,operario,float(importe_repuestos),dato_1,float(dato_2))
    elif tipo == "2":
        mantenim = Correctivo(fecha,operario,float(importe_repuestos),int(dato_1),float(dato_2))
    
    maq.nuevo_mantenimiento(mantenim)

archivo.close()
#print(maq.cantidad_mant())
print("-----REPORTES---------")
print("1- Suma de gastos: $", maq.suma_gastos_mantenim()) 
print("2- Cantidad de mantenimientos caros (mayores a $10000): ", maq.mantenim_caros())
fecha, operario, horas = maq.rot_mas_larga()
print("3- Rotura/s más larga/s: \n cantidad de horas parada:", horas)
for i in range(len(fecha)):
    print("\n fecha:", fecha[i], "\n operario:", operario[i])   
        
    