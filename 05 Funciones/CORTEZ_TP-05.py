#ejercicio 1
#funciones

"""
def mensaje():
    print("Hola Mundo!")
    
#programa principal

print(f"{mensaje()}")

"""
#ejercicio 2
"""
#funciones
#defino la funcion saludar_usuario

def saludar_usuario(nombre):
#se usa el parametro nombre y se agrega texto antes y despues
    return "Hola " + nombre + "!"



#programa principal
n=input("ingrese su nombre= ")
#se llama la funcion en la impresion y se le pasa el argumento n
print(saludar_usuario(n))

"""

#ejercicio 3

"""
#funciones
def informacion_personal(nombre, apellido, edad, residencia):
    return f"soy {nombre} {apellido} tengo {edad} y vivo en {residencia}"

    
#programa principal

nombre=input("ingrese su nombre= ")
apellido=input("ingrese su apellido= ")
edad=input("ingrese su edad= ")
residencia=input("ingrese su residencia= ")
x=informacion_personal(nombre,apellido,edad,residencia)
print(x)


"""


#ejercicio 4
"""


#funciones

import math
#importo la libreria math para usar la funcion pi
def calcular_area(radio):
    area= math.pi * (radio**2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro= (radio*2)*math.pi
    return perimetro



#programa principal

#utilizo la funcion round para limitar hasta 3 decimales
radioi=int(input("ingrese el radio de un circulo"))
area=round(calcular_area(radioi),3)
perimetro=round(calcular_perimetro_circulo(radioi),3)

print(f"el radio ingresado es {radioi}, su area es {area} y su perimetro es {perimetro}")

"""
#ejercicio 5

"""
#funciones

def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas

#programa principal    
    
x=int(input("ingrese la cantidad de segundos que desee= "))
resultado=segundos_a_horas(x)
print(f"{x} segundos son {resultado:.2f} horas")

"""

#ejercicio 6

"""

#funciones


def tabla_multiplicar(numero):
    for x in range(1,11):
        resultado= numero*x
        print(f"{numero} x {x} = {resultado}")
    return

#programa principal  

x=int(input("ingrese el numero que quiere ver su tabla= "))
tabla=tabla_multiplicar(x)

"""
#ejercicio 7

"""


#funciones

def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multi=a*b
    div=a/b

    return (suma, resta, multi, div )

#programa principal 

num1=int(input("ingrese un numero= "))
num2=int(input("ingrese otro numero= "))

resultados = operaciones_basicas(num1,num2)

print("\nResultados:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]:.2f}")

"""

#ejercicio 8

"""

#funciones

def calcular_imc(peso, altura):
    imc=peso / (altura/100)**2
    return imc


#programa principal 

peso=int(input("ingrese su peso"))
altura=float(input("ingrese su altura en cm"))

resultado=calcular_imc(peso,altura)
print(f"segun su peso ({peso}) y su altura ({altura}), su imc es de {resultado:.2f}")

"""

#ejercicio 9

"""

#funciones

def elsius_a_fahrenheit(celsius):
    f=(celsius*1.8)+32
    return f


#programa principal 

c=int(input("ingrese la temperatura en Celsius"))
resultado=elsius_a_fahrenheit(c)
print(f"{c} celsius en fahrenheit seria= {resultado} ")

"""
#ejercicio 10

#funciones

"""

def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    return promedio


#programa principal 

a=int(input("ingrese el primer valor= "))
b=int(input("ingrese el segundo valor= "))
c=int(input("ingrese el tercer valor= "))

resultado=calcular_promedio(a, b, c)

print(f"el promedio de los numeros ingresados({a}, {b}, {c}) es = {resultado:.1f}")

"""