#ejercicio 1 

"""
for x in range(101):
    print(x)

cont=0
while cont <=100:
    print(cont)
    cont=cont+1
"""
#ejercicio 2

"""
num=int(input("ingrese un numero= "))

num=abs(num)
cont=0

if num==0:
    cont=1
else:
    while num>0:
        num=num //10
        cont +=1

print(f"El número tiene {cont} dígito(s).")

"""
#ejercicio3
"""
num1=int(input(" escribe el primer numero= "))
num2=int(input("ingrese el segundo numero= "))
sumatotal=0
for x in range(num1+1,num2):
    sumatotal=sumatotal+x
print("la suma total es= ",sumatotal)
"""
#ejercicio4

sumatotal=0
"""
while True:
    num=int(input("ingrese un numero, si desea terminar ingrese 0"))
    if num==0:
        break;
    sumatotal=sumatotal+num
print("la suma total es: ",sumatotal)
"""
#ejercicio5
"""
import random
cont=0
numrandom=random.randint(1,9)
while True:
    
    adivinar=int(input("Adivine el Numero"))
    cont+=1
    if adivinar == numrandom:
        
        print("*****ACERTASTE*****")
        print("la cantidad de intentos fueron: ",cont)
        break
    else:
    
        print("Intenta nuevamente")
"""

#ejercicio6
"""
for x in range(100,0,-2):
     print(x)
"""

#ejercicio7
"""
num=int(input("ingrese un numero positivo = "))
sumatotal=0
for x in range(1,num):
    print(f"suma= {sumatotal} + {x}")
    sumatotal=sumatotal+x
    
print("la suma total es= ",sumatotal)
"""

#Ejercicio8
"""
cant=int(input("ingrese cuantos numeros quiero analizar "))
pos=0
par=0
impar=0
neg=0
for x in range(cant):
    num=int(input("ingrese un numero"))
    if num<0:
        neg+=1
        if num %2==0:
            par+=1
        else:
            impar+=1
    elif num>0:
        pos+=1
        if num %2==0:
            par+=1
        else:
            impar+=1
    else:
        print("el numero cero no cuenta")
print(f"la cantidad de numeros par es {par}, la cantidad de numeros impar es {impar}")
print(f"la cantidad de numeros positivos es {pos}, la cantidad de numeros negativos es {neg}")

"""  
 
 #Ejercicio9

"""  
cant=int(input("ingrese cuantos numeros quiero analizar "))
suma=0
for x in range(cant):
    num=int(input("ingrese un numero"))
    suma=suma+num
media=suma/cant
print(f"la media de los {num} ingresados es {media}")

"""  

 #Ejercicio10
"""  
num=int(input("ingrese un numero"))
inv = 0
es_negativo = False
if num < 0:
    es_negativo = True
    numero = abs(num) 
while num !=0:
    digito=num%10
    inv= inv*10+digito
    num=num//10
if es_negativo:
    inv *= -1
print("El número invertido es:", inv)
"""  