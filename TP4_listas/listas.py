import random

# Ejercicio 1
# lista con notas
notas = [7, 4, 9, 3, 5, 8, 7, 6, 2, 8]
nota_alta = 0
nota_baja = 10
promedio = 0
suma = 0
for i in notas:
    #suma las notas
    suma = suma + notas[i]
    #si la nota es mas alta, la guarda en la variable
    if nota_alta < notas[i]:
        nota_alta = notas[i]
    # Si la nota es mas baja, la guarda en la variable    
    else:
        nota_baja = notas[i]
# Muestra resultados
promedio = suma / 10
print(f"La nota mas alta fue: {nota_alta}")
print(f"La nota mas baja fue: {nota_baja}")
print(f"El promedio es de: {promedio}")


print()
print()

# Ejercicio 2

# Definimos la lista
productos = []
contador = 0
producto = ""
producto_eliminado = ""
# Pedimos productos al usuario, y lo agregamos a la lista con append()
while contador < 5:
    producto = input("Ingrese un producto: ")
    productos.append(producto)
    contador += 1
# Ordenamos la lista
productos.sort()
print(F"La lista de productos es: {productos}")
# Eliminar productos de la lista
producto_eliminado = input("Que producto desearia eliminar? ")
productos.remove(producto_eliminado)
print(F"La lista de productos actualizada es: {productos}")


print()
print()


# Ejercicio 3

# Creamos las listas
lista_numerica = []
lista_pares = []
lista_impares = []
numero_random = 0

# definimos los 15 numeros randoms
for i in range(15):
    numero_random = random.randint(1,101)
    lista_numerica.append(numero_random)
print(lista_numerica)

# Los agregamos en las listas pares e impares segun el resultado con el metodo .append()
for num in lista_numerica:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

# Mostramos resultados
print(f"La lista de numeros randoms es: {lista_numerica}")
print(f"Los numeros impares de la lista son los siguientes: {lista_impares}")
print(f"Los numeros pares de la lista son los siguientes: {lista_pares}")


print()
print()

# Ejercicio 4

# Creamos las listas
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_unica = []

# Recorremos la lista y si el datos[i] no esta en la lista nueva, lo copiamos
for num in datos:
    if num not in lista_unica:
        lista_unica.append(num)

# Mostramos la lista sin repeticiones
print(f"La lista sin elementos repetitivos es: {lista_unica}")



print()
print()

# Ejercicio 5

# Lista de estudiantes
lista_estudiantes = ["Mario", "Lucia", "Juan", "Pedro", "Maria", "Julia", "Martin", "Franco"]

# Recorremos la lista
for i in lista_estudiantes:
    print(f"La lista de estudiantes es la siguiente: {lista_estudiantes}")
    
    # Preguntamos si se quiere agregar o eliminar estudiantes de la lista
    opcion_agregar = input("Quieres agregar un nuevo estudiante a la lista? (Si/No) ")
    opcion_agregar.lower()
    opcion_eliminar = input("Quieres eliminar un estudiante de la lista? (Si/No) ")
    opcion_eliminar.lower()

    # Agregamos o eliminamos estudiantes segun las opciones elegidas
    if opcion_agregar == "si":
        nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
        lista_estudiantes.append(nuevo_estudiante)
    elif opcion_eliminar == "si":
        eliminar_estudiante = input("Ingrese el nombre del estudiante a eliminar de la lista: ")
        lista_estudiantes.remove(eliminar_estudiante)
    else:
        break
print(f"La lista de estudiantes es la siguiente: {lista_estudiantes}")
        
        
print()
print()


# Ejercicio 7

# Creamos la lista
lista_numerica = [43, 56, 24, 18, 64, 46, 89]

# Creamos una variable temporal para guardar el ultimo elemento de la lista que sera el primero en la nueva lista
temp = lista_numerica[6]

# Se recorre la lista desde el final hacia el inicio, guardado en la posicion[i] el valor de la posicion anterior[i-1]
for i in range(len(lista_numerica) -1, 0, -1):
    lista_numerica[i] = lista_numerica[i - 1]

# Al final, se guarda el valor del ultimo indice grardado en la variable temporal en la primera posicion de la lista
lista_numerica[0] = temp
print(lista_numerica)



print()
print()

# Ejercicio 7

# Creamos las listas
temperaturas = [[12, 7, 9, 3, 10, 14, 5], [27, 22, 18, 25, 29, 17, 24]]
promedio_maximo = 0
promedio_minimo = 0
suma_maxima = 0
suma_minima = 0
amplitud = 0
mayor_amplitud = 0
# Creamos la matriz
for i in range(len(temperaturas)):
    for j in range(len(temperaturas[i])):
        print(temperaturas[i][j], end=" ")

        # Chequeamos si estamos en la fila de minimas o maximas y sumamos los valores en cada una
        if i == 0:
            suma_minima += temperaturas[i][j]
        else:
            suma_maxima += temperaturas[i][j]
        
        # Calculamos la amplitud termica, tomando el indice 1 en i y restandolo con 0 en i, guardando el resultado en amplitud, si esta es mayor que mayor_amplitud, la reemplaza
        amplitud =  temperaturas[1][j] - temperaturas[0][j]
        if amplitud > mayor_amplitud:
            mayor_amplitud = amplitud

    print()

# Calculamos los promedios, dividido el tamaño de temperaturas[0] en ambos ya que al ser una matriz comparten la cantidad de elementos
promedio_minimo = suma_minima / len(temperaturas[0])
promedio_maximo = suma_maxima / len(temperaturas[0])

# Mostramos resultados
print(f"El promedio de las temperaturas minimas es de: {promedio_minimo}")
print(f"El promedio de las temperaturas maximas es de: {promedio_maximo}")
print(f"La mayor amplitud termica fue de: {mayor_amplitud}")


print()
print()


# Ejercicio 8

# Creamos la matriz
notas = [[7, 4, 9],[9, 8, 5],[4, 7 ,3],[8, 6, 9],[9, 4, 6]]

# Creamos variables
suma_notas = 0
suma_materias = 0
promedio_estudiante = []
promedio_materia = []

# Recorremos la matriz desde las filas y sacamos el promedio por estudiante
for estudiante in range(len(notas)):
    for materia in range(len(notas[estudiante])):
        print(notas[estudiante][materia], end=" ")
        suma_notas += notas[estudiante][materia]
               
    print()
    # Calculamos el promedio sumando los valores de la fila y lo dividimos con el total de columnas
    suma_notas = suma_notas / len(notas[0])
    promedio_estudiante.append(suma_notas)

# Recorremos la matriz desde las columnas y sacamos el promedio por materia
for materia in range(len(notas[0])):
    for estudiante in range(len(notas)):
        suma_materias += notas[estudiante][materia]

    # Calculamos el promedio sumando los valores de cada columna y lo dividimos por el total de filas
    suma_materias = suma_materias / len(notas)
    promedio_materia.append(suma_materias)

# Mostramos los resultados
print(f"El promedio de cada estudiante es: {promedio_estudiante}")
print(f"El promedio de cada materia es: {promedio_materia}")


print()
print()


# Ejercicio 9

# Creamos el tablero
lista_tablero = [["-","-","-"],["-","-","-"], ["-","-","-"]]

# Creamos las variables
player1 = "X"
player2 = "O"
posicion_col = 0
posicion_fil = 0
tablero_completo = 0

# Recorremos con bucle while para que se siga imprimiendo el tablero, de caso contrario habria que usar una funcion de impresion
while tablero_completo <= 4:
    # Imprimimos el tablero
    for fila in range(len(lista_tablero)):
        for columna in range(len(lista_tablero[0])):
            print(lista_tablero[fila][columna],end=" ")
        print()
    # Pedimos la posicion en donde poner la X del player1    
    posicion_fil = int(input("Jugador 1, en que fila quisiera poner una jugada? (0, 1, 2) "))
    posicion_col = int(input("Jugador 1, en que columna quisiera poner una jugada? (0, 1 o 2) "))
    lista_tablero[posicion_fil][posicion_col] = player1
    # Volvemos a imprimir el tablero para mostrar resultados
    for fila in range(len(lista_tablero)):
        for columna in range(len(lista_tablero[0])):
            print(lista_tablero[fila][columna],end=" ")
        print()
    # Pedimos la posicion en donde poner la O del player2    
    posicion_fil = int(input("Jugador 2, en que fila quisiera poner una jugada? (0, 1 o 2) "))
    posicion_col = int(input("Jugador 2, en que columna quisiera poner una jugada? (0, 1 o 2) "))
    lista_tablero[posicion_fil][posicion_col] = player2
    tablero_completo += 1
    

print()
print()

# Ejercicio 10

# Creamos la matriz de 7x4
matriz_ventas = [[100, 120, 150, 130, 200, 180, 220],
                 [80, 90, 70, 85, 100, 120, 120],
                 [200, 210, 220, 230, 240, 220, 220],
                 [50, 60, 55, 70, 80, 100, 110]]

# declaramos las variables
total_venta_prod = []
total_venta = 0
prod_mas_vendido = 0
posicion = 0
prod_mas_vendido_sem = []
prod_mas_vendido_dia = 0

# Recorremos la matriz y la mostramos en pantalla
for fil in range(len(matriz_ventas)):
    for col in range(len(matriz_ventas[0])):
        print(matriz_ventas[fil][col], end=" ")
        #guardamos el total de venta de cada producto en una nueva lista
        total_venta += matriz_ventas[fil][col]
    total_venta_prod.append(total_venta)
    print()
# Mostramos el todal de venta de cada producto    
print(f"""El total de ventas de cada producto fue de: Producto 1: {total_venta_prod[0]}
 Producto 2: {total_venta_prod[1]} Producto 3: {total_venta_prod[2]} Producto 4: {total_venta_prod[3]}""")

# Recorremos la lista de los totales de venta, con la funcion enumerate() para que nos deje pasarle la posicion y asi detectar cual producto es el mas vendido
for i, producto in enumerate(total_venta_prod):
    if producto > prod_mas_vendido:
        prod_mas_vendido = producto
        posicion = i
# Mostramos los resultados en pantalla        
print(f"El producto mas vendido en la semana es el que esta en la posicion {posicion}, con un total de $ {prod_mas_vendido} en ventas.")

# Recorremos la matriz desde las columnas a las filas
for col in range(len(matriz_ventas[0])):
    for fil in range(len(matriz_ventas)):
        # Guardamos la suma de los productos vedidos en cada dia en una nueva lista agregandolos con .append()
        prod_mas_vendido += matriz_ventas[fil][col]
    prod_mas_vendido_sem.append(prod_mas_vendido)

# Recorremos la nueva lista usando enumerate() para conocer el indice y el valor
for i, dia in enumerate(prod_mas_vendido_sem):
    if dia > prod_mas_vendido_dia:
        prod_mas_vendido_dia = dia
        posicion = i

# Controlamos que posicion tiene el mayor numero de ventas y con eso nos da el dia de la semana
if posicion == 0:
    print(f"El dia con mayor ventas fue el lunes con ${prod_mas_vendido}")
elif posicion == 1:
    print(f"El dia con mayor ventas fue el Martes con ${prod_mas_vendido}")
elif posicion == 2:
    print(f"El dia con mayor ventas fue el Miercoles con ${prod_mas_vendido}")
elif posicion == 3:
    print(f"El dia con mayor ventas fue el Jueves con ${prod_mas_vendido}")
elif posicion == 4:
    print(f"El dia con mayor ventas fue el Viernes con ${prod_mas_vendido}")
elif posicion == 5:
    print(f"El dia con mayor ventas fue el Sabado con ${prod_mas_vendido}")
elif posicion == 6:
    print(f"El dia con mayor ventas fue el Domingo con ${prod_mas_vendido}")