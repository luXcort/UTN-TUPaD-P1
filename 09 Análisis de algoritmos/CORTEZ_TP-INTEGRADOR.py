import random
import time

def generar_lista(tamano):
    return random.sample(range(1, tamano * 10), tamano)


def crear_lista_ordenada(n):
    return list(range(1, n + 1))

def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i, valor in enumerate(lista):
        comparaciones += 1
        if valor == objetivo:
            return i, comparaciones
    return -1, comparaciones


def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, comparaciones

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Generar nueva lista")
    print("2. Crear lista ordenada del 1 al n")
    print("3. Buscar (lineal)")
    print("4. Buscar (binaria)")
    print("5. Mostrar lista")
    print("6. Salir")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            n = int(input("Tamaño de la lista: "))
            lista = generar_lista(n)
            print("Lista generada.")

        elif opcion == "2":
                n = int(input("¿Hasta qué número querés la lista ordenada?: "))
                lista = crear_lista_ordenada(n)
                print(f"Lista del 1 al {n} creada.")


        elif opcion == "3":
            if not lista:
                print("Primero generá una lista.")
                continue
            objetivo = int(input("Número a buscar: "))
            inicio = time.perf_counter()
            posicion, comparaciones = busqueda_lineal(lista, objetivo)
            fin = time.perf_counter()
            print(f"Resultado: {'Encontrado en índice ' + str(posicion) if posicion != -1 else 'No encontrado'}")
            print(f"Comparaciones: {comparaciones}")
            print(f"Tiempo: {(fin - inicio)*1000:.4f} milisegundos")

        elif opcion == "4":
            if not lista:
                print("Primero generá una lista random.")
                continue
            lista.sort()
            objetivo = int(input("Número a buscar: "))
            inicio = time.perf_counter()
            posicion, comparaciones = busqueda_binaria(lista, objetivo)
            fin = time.perf_counter()
            print(f"Resultado: {'Encontrado en índice ' + str(posicion) if posicion != -1 else 'No encontrado'}")
            print(f"Comparaciones: {comparaciones}")
            print(f"Tiempo: {(fin - inicio)*1000:.4f} milisegundos")

        elif opcion == "5":
            if lista:
                print(lista)
            else:
                print("La lista está vacía.")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()