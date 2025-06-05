#Ejercicio 1
"""
edad=int(input	("ingrese su edad: "))
if edad >=18:
    print("Es mayor de edad")
"""

#Ejercicio 2
"""
nota=int(input("ingrese su nota: "))
if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")
   """ 
    
#Ejercicio 3
"""
numero=int(input("ingrese numeros pares"))
if numero%2==0:
    print("Ha ingresado un número par")
else:
    print("porfavor, ingrese un número par")
""" 
#Ejercicio 4
""" 
edad=int(input	("ingrese su edad: "))
if edad <12:
    print("Niño/a: menor de 12 años.")
elif edad>=12 and edad<18:
   print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif edad>=18 and edad<30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif edad>=30:
    print("Adulto/a: mayor o igual que 30 años.")
else:  
   print("ingreso un numero incorrecto")
""" 
#Ejercicio 5
""" 
contrasena=input("ingrese su contraseña")

if len(contrasena)>=8 and len(contrasena)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("porfavor, ingrese una contraseña entre 8 y 14 caracteres")
""" 
#Ejercicio 6
""" 
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(10)]
print("los numeros aleatorios son: ",numeros_aleatorios)
media=mean(numeros_aleatorios)
mediana=median(numeros_aleatorios)
moda=mode(numeros_aleatorios)
print("la media es:",media)
print("la mediana es:",mediana)
print("la moda es:",moda)

if media>mediana and mediana >moda:
    print("Sesgo positivo")
elif media<mediana and mediana<moda:
    print("Sesgo Negativo")
elif media==mediana==moda:
    print("Sin Sesgo")
else:
    print("fuera de criterio")
""" 

#Ejercicio 7
""" 
frase=input("ingrese una palabra o frase: ")
ultimaletra=frase[-1]
if ultimaletra=="a" or ultimaletra=="e" or ultimaletra=="i" or ultimaletra=="o" or ultimaletra=="u":
    frase=frase+"!"
    print(frase)
else:
    print(frase)
""" 

#Ejercicio 8
""" 
nombre=input("Ingrese su nombre: ")
print("Bienvenido ",nombre)

print("1-Su nombre en mayusculas ")
print("2-Su nombre en minusculas ")
print("3-La inicial de su nombre en mayusculas ")
opcion=int(input("***Seleccione una opcion: ***  "))

if opcion==1:
    nombre=nombre.upper()
    print(nombre)
elif opcion==2:
    nombre=nombre.lower()
    print(nombre)
elif opcion==3:
    nombre=nombre.title()
    print(nombre)
else:
    print("opcion incorrecta")

""" 
#Ejercicio 9
"""
magnitud=int(input("ingrese la magnitud del terremoto: "))
if magnitud<3 and magnitud>0:
    print("Muy leve - imperceptible")

elif magnitud>=3 and magnitud<4:
    print("Leve (ligeramente perceptible)")

elif magnitud>=4 and magnitud<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")

elif magnitud>=5 and magnitud<6:
    print("Fuerte (puede causar daños en estructuras débiles).")

elif magnitud>=6 and magnitud<7:
    print("Muy Fuerte (puede causar daños significativos)")

elif magnitud>=7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("ingrese una magnitud correcta")
"""
#Ejercicio 10
"""
print("indique en que hemisferio se encuentra?")
hemisferio=input("N=Norte ------ S=Sur  =")
mes=int(input("ingrese en que mes esta: "))
dia=int(input("ingrese en que dia esta: "))

if hemisferio.upper()=="N":
    if mes==12 and dia>=21 or mes==1 or mes==2 or mes==3 or mes==4 and dia<=20: 
        print("Invierno del hemisferio norte")
    elif mes==4 and dia>=21 or mes==5 or mes==6 and dia<=20: 
        print("Primavera del hemisferio norte")
    elif mes==6 and dia>=21 or mes==7 or mes==8 or mes==9 and dia<=20: 
        print("Verano del hemisferio norte")
    elif mes==9 and dia>=21 or mes==10 or mes==11 or mes==12 and dia<=20: 
        print("Otoño del hemisferio norte")
elif hemisferio.upper()=="S":
    if mes==12 and dia>=21 or mes==1 or mes==2 or mes==3 or mes==4 and dia<=20: 
        print("Verano del hemisferio Sur")
    elif mes==4 and dia>=21 or mes==5 or mes==6 and dia<=20: 
        print("Otoño del hemisferio Sur")
    elif mes==6 and dia>=21 or mes==7 or mes==8 or mes==9 and dia<=20: 
        print("Invierno del hemisferio Sur")
    elif mes==9 and dia>=21 or mes==10 or mes==11 or mes==12 and dia<=20: 
        print("Primavera del hemisferio Sur")
else:
    print("incorrecto")
"""