# encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion:Imprimir la combinación de 2 colores
#Funcion que ve la combinacion de los valores
def colorC(co1, co2):
    if co1 == str("amarillo") or co2 == str ("amarillo") or co1 == str("AMARILLO") or co2 == str ("AMARILLO"):
        if co1 == str("rojo") or co2 == str ("rojo") or co1 == str("ROJO") or co2 == str ("ROJO"):
            colorf = ("naranja")
    elif co1 == str("rojo") or co2 == str ("rojo") or co1 == str("rojo") or co2 == str ("rojo"):
        if co1 == str("azul") or co2 == str ("azul") or co1 == str("AZUL") or co2 == str ("AZUL"):
            colorf = ("morado")
    elif co1 == str("azul") or co2 == str ("azul") or co1 == str("AZUL") or co2 == str ("AZUL"):
        if co1 == str("amarillo") or co2 == str ("amarillo") or co1 == str("AMARILLO") or co2 == str ("AMARILLO"):
            colorf = ("verde")
    return colorf
#iprime el color, lee los inputs
def main():
    color1 = str(input("Escribe el color 1:"))
    color2 = str(input("Escribe el color 2:"))
    colf = colorC(color1,color2)
    print(colf)

main()