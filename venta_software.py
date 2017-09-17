# encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion:Calcular costo de paquetes con descvuento
#recibe cantidad de paquetes y calcula costo total
def costoT(paquetes):
    if paquetes >= 1:
        if paquetes >=10 and paquetes <= 19:
            precio = (paquetes * 1500) * .80
        elif paquetes >=20 and paquetes <= 49:
            precio = (paquetes * 1500) * .70
        elif paquetes >= 50 and paquetes <= 99:
            precio = (paquetes * 1500) * .60
        elif paquetes >= 100:
            precio = (paquetes * 1500) * .50
    else:
        print("Error")
    return  precio
#Funcion que lee input, imprime el costo y marca solo valores positivos
def main():
    paquetes = int(input("Escribe el numeror de paquetes comprados:"))
    if paquetes >= 1:
        print("El costo total es:", costoT(paquetes))
    else:
        print("Error, ponga un valor positivo")
main()

