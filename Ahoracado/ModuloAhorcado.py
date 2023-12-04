def mostrarArray(array):
    for i in range(len(array)):
        print(array[i], end="")


def comprobarPal(palabraGuion):
    for i in range(len(palabraGuion)):
        if palabraGuion[i] == "_":
            return False
    return True


def mostrarGuiones(palabra):
    pal = []
    for i in range(len(palabra)):
        pal.append("_")
    return pal


def validar_caracter():
    while True:
        caracter = input("\nIngrese un solo caracter: ")
        if len(caracter) == 1:
            return caracter
        else:
            print("\nPor favor, ingrese solo un caracter.")


def pantalla(cont):
    if cont == 1:
            print("\nAdivinaste una letra", end="\t\t\t\t\t\t\t\t")

    if cont > 1:
            print("\nAdivinaste", cont, "letras", end="\t\t\t\t\t\t\t\t")


def chequeoVidas(cont, vidas):
    if cont == 0:
        vidas -= 1
    return vidas


