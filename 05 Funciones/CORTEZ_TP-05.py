#Ejercicio 1

""" 
# creo una lista con limites de 0 a 101 y que vaya salteando de 4 en 4 
multi4=list(range(0,101,4))
print(multi4)
"""  

#Ejercicio 2

""" 
jugadores=["burruchaga","delamata","mondragon","trossero","bochini"]
#utilizo el indice -1 para indicarle que traiga el ultimo, ya que al utilizar negativo da vuelta la lista
print(jugadores[-1])
""" 


#Ejercicio3
""" 
#creo la lista vacia
lista=[]
#recorro un for 3 veces
for i in range (3):
    num=int(input("ingrese un numero: "))
    #solicito un numero y lo agrego con append en la lista 
    lista.append(num)
print("su lista es=", lista)

""" 

#Ejercicio4

""" 
animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
#utilizamos numeros negativos para acceder al ultimo elemento
animales[-1]="oso"
print("su lista es",animales)

""" 

#Ejercicio5

""" 

# se crea una lista con 5 elementos, todos numeros enteros
numeros = [8,15,3,22,7]

# se llama la lista y se utiliza la sentencia remove para eliminar un elemento con el parametro max que busca en la lista el valor mas alto
numeros.remove(max(numeros))

#se imprimen los elementos de la lista
print(numeros)

""" 

#Ejercicio6

"""

#se crea la lista de 10 a 31 para que incluya el 30, y se indica que haga saltos de 5 en 5
num=list(range(10,31,5))

#se imprime los elemento desde el primero al segundo
print(num[0:2])

"""
#Ejercicio7

"""

autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1]="tiida"
autos[2]="uno"
print(autos)

"""
#Ejercicio8


"""

doble=[]

# Agrego el doble de 5, 10 y 15 usando append
doble.append(5*2)
doble.append(10*2)
doble.append(15*2)

print(doble)

"""


#Ejercicio9

"""

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
print(compras)
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.

compras[1][1]="tallarines"
print(compras)

#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
#tambien se puede eliminar de la siguiente forma usando directamente los indices
#del compras[0][0]

#d) Imprimir la lista resultante por pantalla
print(compras)

"""
#Ejercicio9
#se crea la lista con los elementos, dentro se crea otra lista con los demas elementos
lista_aninada=[15,True,[25.5,57.9,30.6],False]
#se imprime como se mostro en la consigna

print(lista_aninada[0])
print(lista_aninada[1])
print(lista_aninada[2][0])
print(lista_aninada[2][1])
print(lista_aninada[2][2])
print(lista_aninada[3])

#se imprime la lista completa
print(lista_aninada)