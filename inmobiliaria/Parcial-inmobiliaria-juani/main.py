from inmobiliaria import Inmobiliaria

def main():
    
    inmobiliaria = Inmobiliaria()
    
    archivo = open("inmuebles.csv")
    
    for linea in archivo.readlines():
        inmobiliaria.agregar_inmueble(linea)
    
    archivo.close()
    
    print("Suma de Alquileres: $" + str(inmobiliaria.suma_alq()))
    print("Cantidad de Casas Premium: " + str(inmobiliaria.casa_premium()))
    print("Propietario Departamento Economico: " + inmobiliaria.menor_alquiler())
        

if __name__ == "__main__":
    main()