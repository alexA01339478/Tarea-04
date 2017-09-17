# encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion: Calcular indice de masa corporal
#Funcion que calcula imc con la estatura y el peso escritos
def calcularIMC(peso, altura):
    if peso >= 1 and altura >= 1:
        iMC = peso / (altura ** 2)
    return iMC
#Funcion que recibe input, determina en que valores de imc estas y el estado en el que estas
def main():
    peso = float(input("Pon tu peso en Kilogramos:"))
    altura = float(input("Pon tu altura en metros"))
    if peso > 0 and altura >0:
        if calcularIMC(peso, altura) < 18.5:
            print("Tienes un peso bajo:", calcularIMC(peso, altura), ("IMC"))
        elif calcularIMC(peso, altura) >= 18.5 and calcularIMC(peso, altura) <=25:
            print("Tienes un peso normal:", calcularIMC(peso, altura), ("IMC"))
        elif calcularIMC(peso, altura) < 25:
            print("Tienes sobrepeso:", calcularIMC(peso, altura), ("IMC"))
    else:
        print("Pon valores de peso y altura validos")

main()