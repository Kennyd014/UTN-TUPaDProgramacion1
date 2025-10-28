# Ejercicio 1

# diccionario de datos
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

# Añadir datos
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2

# Modificar elementos
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3

# Lista de frutas
lista_frutas = precios_frutas.keys()


# Ejercicio 4
directorio = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero de telefono del contacto: ")
    directorio[nombre] = numero

# Buscar contacto
contacto = input("Ingrese el nombre del contacto a buscar: ")

if contacto in directorio:
     print(f"{contacto}: {directorio[contacto]}")
else:
        print("No se encuentra el contacto")
print(directorio)

# Ejercicio 5

# Palabras unicas en una frase
frase = input("Ingrese una frase: ")
# Se divide la frase en palabras
palabras = frase.split()
# Se guardan solo las palabras sin su repeticion
palabras_unicas = set(palabras)
print(f"Palabras unicas: {palabras_unicas}")

# Diccionario con palabras repetidas
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(f"Recuento: {conteo_palabras}")

# Ejercicio 6
alumnos = {}

for i in range(3):
    estudiante = input("Ingrese el nombre del estudiante: ")
    notas = []
    for j in range(3):
        nota = float(input("Ingresar la nota: "))
        notas.append(nota)
        alumnos[estudiante] = tuple(notas)
print(alumnos)
# Sacar promedio
for estudiante, notas in alumnos.items():
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / 3
    print(f"El Promedio de {estudiante} es: {promedio:.2f}")


# Ejercicio 7

# Set de estudiantes
parcial1 = {'Pablo','Maria','Juan','Pedro','Nicole','Andrea'}
parcial2 = {'Martin','Andrea','Juan','Maria','Jose'}

# Aprobaron ambos parciales
ambos_parciales = parcial1 & parcial2
print("Los estudiantes que aprobaron ambos parciales son: ",ambos_parciales)
# Aprobaron solo un parcial
solo_un_parcial = parcial1 ^ parcial2
print("Los estudiantes que aprobaron solo un parcial son: ",solo_un_parcial)
# Aprobaron al menos un parcial
al_menos_un_parcial = parcial1 | parcial2
print("Los estudiantes que aprobaron al menos un parcial son: ",al_menos_un_parcial)



# Ejercicio 8

# Diccionario
stock_productos = {"remeras": 30, "jeans": 15, "shorts": 17}

# Lista para el menu
menu = [""" 
        1. Consultar stock
        2. Agregar unidades a un producto existente
        3. Agregar un nuevo producto
        4. Salir
"""
]

# programa principal
while True:
    opcion = input("Ingrese una opcion valida: ")

    for seleccion in menu:
        print(seleccion)

    match opcion:
        # Consultar stock del producto
        case '1':

            producto = input("Ingrese el nombre del producto: ").lower().strip()
            if producto in stock_productos:
                print(f"El Stock de {producto} es de {stock_productos[producto]} unidades")
            else:
                print(f" El producto {producto} no se encuentra en el inventario")
        # Agregar unidades al stock de un producto existente
        case '2':

            producto = input("Ingrese el nombre del producto: ").lower().strip()
            if producto in stock_productos:
                cantidad = int(input(f"Ingrese cuantas unidades desea agregar de {producto}: "))
                stock_productos[producto] += cantidad
                print(f"El stock actualizado de {producto} es de {stock_productos[producto]} unidades")
            else:
                print(f" El producto {producto} no se encuentra en el inventario")
        # Agregar producto nuevo con unidades
        case '3':

            producto = input("Ingrese el nombre del nuevo producto: ").lower().strip()
            if producto in stock_productos:
                print("El producto ya se encuentra en el inventario")
            else:
                cantidad = int(input(f"Ingrese cuantas unidades desea agregar de {producto}: "))
                stock_productos[producto] = cantidad
                print(f"Producto {producto} agregado con {stock_productos[producto]} unidades")
        # Salir
        case '4':

            print("Saliendo del programa...")
            break
        # Caso default
        case _:
            print("Opcion invalida, por favor ingrese una opcion valida: ")
            


# Ejercicio 9

# Diccionario agenda
agenda = {
    ('lunes', '09:00'): 'Meeting',
    ('lunes', '15:00'): 'GYM',
    ('miercoles', '12:00'): 'Almuerzo con clientes',
    ('viernes', '18:00'): 'Futbol con amigos',
    ('sabado', '20:00'): 'Asado con los chicos'
}

# Menu
while True:
    print("1.Consultar actividad")
    print("2.Salir")
    seleccion = input("Ingrese una opcion valida: ")
    match seleccion:
        case '1':
            dia = input("Ingrese el dia de la semana: ").lower().strip()
            hora = input("Ingrese la hora (en formato HH:MM): ")
            clave = (dia,hora)
            if clave in agenda:
                print(f"La actividad para el {dia} a las {hora} hs es {agenda[clave]}")
            else:
                print("No hay actividades registradas para ese dia")
        case '2':
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida, por favor ingrese una opcion valida")


# Ejercicio 10

# Diccionario de paises y capitales

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Italia": "Roma",
    "Francia": "París",
    "Japón": "Tokio"
}

# Nuevo diccionario invertido
capitales_paises = {}

# Bucle para ir guardando los elemetos en el nuevo diccionario
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

