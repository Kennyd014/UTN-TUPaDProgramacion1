# Ejercicio 1
"""
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

"""
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