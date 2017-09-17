# encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion: Recibir numeror decimal y mostrar determinado numero en romano
#Funcion que convierte de decimal a romano
def calcularN(numero):
    if numero <= 3:
        numeroR = (numero * "I")
    elif numero ==4:
        numero = 1
        numeroR = (numero * "I") + str("V")
    elif numero >= 5 and numero <= 8:
        numeroR = str("V") + ((numero - 5) * "I")
    elif numero ==9:
        numero = 1
        numeroR = (numero * "I") + ("X")
    elif numero == 10:
        numeroR = ("X")
    else:
        print("Error")
    return numeroR
#Funcion que lee input, regresa valores, delimitan que valores se pueden usar e imprime el resultado
def main():
    numero = int(input("Escribe tu número:"))
    if numero >=1 and numero <= 10:
        print("Número en romano:", calcularN(numero))
    else:
        print("Error, ponga valores del 1 al 10")

main()