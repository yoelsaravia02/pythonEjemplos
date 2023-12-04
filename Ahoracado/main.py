from Ahoracado.ModuloAhorcado import *


def test():
    palabra = input("Ingrese la palabra a adivinar: ")
    palabraGuion = mostrarGuiones(palabra)
    adivinanza = False
    vidas = 6
    while not adivinanza:
        let = validar_caracter()
        cont = 0
        for i in range(len(palabra)):
            if let == palabra[i]:
                # ADIVINO LA LETRA
                cont += 1
                palabraGuion[i] = let

        if cont == 0:
            vidas -= 1
            print("Ahora tienes", vidas, "vidas")
        if vidas == 0:
            print("Te has quedado sin vidas ...")
            break
        pantalla(cont)
        mostrarArray(palabraGuion)
        flag = comprobarPal(palabraGuion)
        if flag:
            print("\nFELICITACIONES !!!")
            print("Haz ganado el juego").upper()
            break
    print("Haz perdido el juego").upper()


if __name__ == '__main__':
    test()
