# encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion: Programa que lee largo y ancho de 2 rectangulos, los dibuja, muestra area y perimetro y compara el de mayor area

import turtle
turtle.shape("turtle")
#Funciones para dibujar rectangulos
def drawR1(m1, m2):
    turtle.pencolor("red")
    turtle.forward(m2)
    turtle.left(90)
    turtle.forward(m1)
    turtle.left(90)
    turtle.forward(m2)
    turtle.left(90)
    turtle.forward(m1)
    turtle.left(90)

def drawR2(m1, m2):
    turtle.pencolor("blue")
    turtle.forward(m2)
    turtle.left(90)
    turtle.forward(m1)
    turtle.left(90)
    turtle.forward(m2)
    turtle.left(90)
    turtle.forward(m1)
    turtle.left(90)
#Funciones para calcular area y perimetro
def rectanguloA(medidas1, medidas2):
    area = medidas1 * medidas2
    return area
def rectanguloP(medidas1, medidas2):
    perimetro = (medidas1 * 2) + (medidas2 * 2)
    return perimetro
#Funcion que lee los input, regresa los valores, imprime los valores, y compara que triangulo es mayor
def main():
    largo = int(input("Largo del rectangulo 1:"))
    ancho = int(input("Ancho del rectangulo 1:"))
    ancho2 = int(input("Ancho del rectangulo 2:"))
    largo2 = int(input("Largo del rectangulo 2:"))
    rectangulo1A = rectanguloA(largo, ancho)
    rectangulo2A = rectanguloA(largo2, ancho2)
    rectangulo1P = rectanguloP(largo, ancho)
    rectangulo2P = rectanguloP(largo2, ancho2)
    print("Area rectangulo 1:", rectangulo1A,"cm")
    print("Perimetro rectangulo 1:", rectangulo1P,"cm")
    print("Area rectangulo 2:", rectangulo2A, "cm")
    print("Perimetro rectangulo 2:", rectangulo2P, "cm")
    if rectangulo1A < rectangulo2A:
        print("El rectangulo 2 tiene mayor area")
    elif rectangulo2A == rectangulo1A:
        print("Los rectangulos tienen la msima area")
    else:
        print("El rectangulo 1 tiene mayor area")
    if largo2 > 0:
        drawR1(largo, ancho)
        drawR2(largo2, ancho2)
        turtle.exitonclick()
main()