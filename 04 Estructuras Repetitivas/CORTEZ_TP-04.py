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

num=int(input("ingrese un numero positivo = "))
sumatotal=0
for x in range(1,num):
    print(f"suma= {sumatotal} + {x}")
    sumatotal=sumatotal+x
    
print("la suma total es= ",sumatotal)