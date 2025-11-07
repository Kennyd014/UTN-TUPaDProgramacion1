import csv
import os

NOMBRE_ARCHIVO = "datos_paises.csv"

# Lista para el menu
menu = [
          "1. Agregar nuevo pais",
          "2. Actualizar datos",
          "3. Buscar pais por nombre",
          "4. Mostrar lista de paises",
          "5. Ordenar paises",
          "6. Mostrar estadisticas",
          "7. Salir"
]

sub_menu_actualizar = [
    "1. Actualizar datos de poblacion",
    "2. Actualizar datos de superficie",
    "3. Volver al menu anterior"
]

sub_menu_listado = [
    "1. Mostrar lista completa",
    "2. Filtrar listado por continente",
    "3. Filtrar listado por rango de poblacion",
    "4. Filtrar listado por rango de superficie",
    "5. Volver al menu anterior"
]

sub_menu_ordenamiento = [
    "1. Ordenar paises por nombre",
    "2. Ordenar paises por poblacion",
    "3. Ordenar paises por superficie",
    "4. Volver al menu anterior"
]

sub_menu_estadisticas = [
    "1. Mostrar pais con mayor y menor poblacion",
    "2. Mostrar promedio de poblacion",
    "3. Mostrar promedio de superficie",
    "4. Mostrar cantidad de paises por continente",
    "5. Volver al menu anterior"
]



# Funciones auxiliares

# Obtener datos_paises
def obtener_datos():

    # lista en donde se guardaran los datos importados del archivo csv
    listado_paises = []

    # Si el archivo no existe, lo crea, con los campos de nombre, poblacion, superficie y continente
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'w', newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
            escritor.writeheader()
            return listado_paises
    
    # Si el archivo ya existe, lo muestra    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            listado_paises.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]),"continente": fila["continente"]})
    return listado_paises

# Guardar item
def guardar_item(paises):
    with open(NOMBRE_ARCHIVO, 'w', newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
        escritor.writeheader()
        escritor.writerows(paises)

# Agregar_nuevo_pais
def agregar_nuevo_pais(nuevo_pais):
    with open(NOMBRE_ARCHIVO, 'a', newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
        escritor.writerow(nuevo_pais)
        
# Verifica si el pais ya existe
def existe_pais(nuevo_pais):
    paises = obtener_datos()

    for pais in paises:
        if pais["nombre"].lower() == nuevo_pais.strip().lower():
            return True
    
    return False

# Valida que no este vacio el input
def validar_vacio(nuevo_pais):
    if nuevo_pais == "":
        return False
    
    return True

# Validar numero
def validar_numero(cantidad):
    if not cantidad.isdigit():
        return False
    
    return True

# Validar lista vacia
def validar_datos():
    paises = obtener_datos()
    if not paises:
        print("Aún no hay paises ingresados. Por favor, ingrese un pais primero para luego poder actualizar los datos de poblacion y superficie")

# Mostrar lista completa
def mostrar_lista_completa():
    paises = obtener_datos()

    # Validacion de lista vacia
    validar_datos()

    print("---Listado de paises---")    
    for pais in paises:
        print(f"PAIS: {pais['nombre'].upper()} - POBLACION: {pais['poblacion']} - SUPERFICIE: {pais['superficie']} - CONTINENTE: {pais['continente'].upper()}")

# Actualizar datos poblacion
def actualizar_poblacion():
    # Obtenemos la los datos
    paises = obtener_datos()
    # Validar lista vacia
    validar_datos()

    # Pedir datos al usuario
    pais = input("Ingrese el nombre del pais: ").strip()

    # Validad input vacio
    if not pais:
        print("Por favor, ingrese un pais")
    
    # actualizamos datos
    encontrado = False
    for item in paises:
        if item['nombre'].lower() == pais.lower():
            poblacion = input("Ingrese la poblacion: ").strip()
            encontrado = True
            if not validar_numero(poblacion):
                print("Datos ingresados invalidos")
                return
            poblacion = int(poblacion)
            item['poblacion'] = poblacion
            guardar_item(paises)

            print(f"Se actualizo correctamente la poblacion de {pais}, ahora es de: {poblacion}")
    if not encontrado:
        print("No se encuentra el pais en la lista\n")

# Actualizar datos superficie
def actualizar_superficie():
    # Obtenemos la los datos
    paises = obtener_datos()
    # Validar lista vacia
    validar_datos()

    # Pedir datos al usuario
    pais = input("Ingrese el nombre del pais: ").strip()

    # Validad input vacio
    if not pais:
        print("Por favor, ingrese un pais")
    
    # actualizamos datos
    encontrado = False
    for item in paises:
        if item['nombre'].lower() == pais.lower():
            superficie = input("Ingrese la superficie: ").strip()
            encontrado = True
            if not validar_numero(superficie):
                print("Datos ingresados invalidos")
                return
            superficie = int(superficie)
            item['superficie'] = superficie
            guardar_item(paises)

            print(f"Se actualizo correctamente la poblacion de {pais}, ahora es de: {superficie}")
    if not encontrado:
        print("No se encuentra el pais en la lista\n")

# Filtrar por continente
def filtrar_continente():
    paises = obtener_datos()

    # Validacion de lista vacia
    validar_datos()
    #Pedir datos al usuario
    continente = input("Ingrese el continente: ").strip()
    print("---Listado de paises---") 
    encontrado = False   
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            encontrado = True
            print(f"PAIS: {pais['nombre'].upper()} - POBLACION: {pais['poblacion']} - SUPERFICIE: {pais['superficie']} - CONTINENTE: {pais['continente'].upper()}")
    if not encontrado:
        print("No hay ningun pais perteneciente a ese continente\n")

# Filtrar por rango de poblacion
def rango_poblacion():
    paises = obtener_datos()

    # Validacion de lista vacia
    validar_datos()
    #Pedir datos al usuario
    rango_min = input("Ingrese el rango minimo de poblacion: ").strip()
    rango_max = input("Ingrese el rango maximo de poblacion: ").strip()
     # Validacion de numeros
    if not validar_numero(rango_min):
        print("Datos ingresados invalidos")
        return
    if not validar_numero(rango_max):
        print("Datos ingresados invalidos")
        return
    rango_min = int(rango_min)
    rango_max = int(rango_max)
    print()
    print("---Listado de paises---") 
    encontrado = False   
    for pais in paises:
        if rango_min <= pais['poblacion'] <= rango_max:
            encontrado = True
            print(f"PAIS: {pais['nombre'].upper()} - POBLACION: {pais['poblacion']} - SUPERFICIE: {pais['superficie']} - CONTINENTE: {pais['continente'].upper()}")
    if not encontrado:
        print("No hay ningun pais perteneciente a ese rango\n")

# Filtrar por rango de superficie
def rango_superficie():
    paises = obtener_datos()

    # Validacion de lista vacia
    validar_datos()
    #Pedir datos al usuario
    rango_min = input("Ingrese el rango minimo de superficie: ").strip()
    rango_max = input("Ingrese el rango maximo de superficie: ").strip()
     # Validacion de numeros
    if not validar_numero(rango_min):
        print("Datos ingresados invalidos")
        return
    if not validar_numero(rango_max):
        print("Datos ingresados invalidos")
        return
    rango_min = int(rango_min)
    rango_max = int(rango_max)
    print("---Listado de paises---") 
    encontrado = False   
    for pais in paises:
        if rango_min <= pais['superficie'] <= rango_max:
            encontrado = True
            print(f"PAIS: {pais['nombre'].upper()} - POBLACION: {pais['poblacion']} - SUPERFICIE: {pais['superficie']} - CONTINENTE: {pais['continente'].upper()}")
    if not encontrado:
        print("No hay ningun pais perteneciente a ese rango\n")










##############################################

# Funciones del menu

# Agregar nuevo pais
def agregar_pais():
   while True:
       print("---Ingrese el nuevo pais---")
       nuevo_pais = input("Ingrese el nuevo pais: ").strip().lower()

       if existe_pais(nuevo_pais):
           print("El pais ya se encuentra agregado")
           return
       
       # Validar vacio
       if not validar_vacio(nuevo_pais):
           print("El pais ingresado no es valido")
           return
       
       # Ingresar poblacion
       poblacion = input("Ingrese la poblacion: ").strip()
       # validar numero
       if not validar_numero(poblacion):
           print("Los datos ingresados no son validos")
           return
       poblacion = int(poblacion)

       # Ingresar superficie
       superficie = input("Ingrese la superficie en km2: ").strip()
       # validar numero
       if not validar_numero(superficie):
           print("Los datos ingresados no son validos")
           return
       superficie = int(superficie) 

       # Ingresar continente
       continente = input("Ingrese el continente: ").strip()

       # Agregar datos
       agregar_nuevo_pais({'nombre': nuevo_pais, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente})
       print(f"Se agrego correctamente {nuevo_pais} a la lista")
       break


# Actualizar datos
def actualizar_datos():
    mostrar_submenu_actualizar()

# Buscar pais
def buscar_pais():
    # Obtenemos la los datos
    paises = obtener_datos()
    # Validar lista vacia
    validar_datos()

    # Pedir datos al usuario
    pais = input("Ingrese el nombre del pais: ").strip()

    # Validad input vacio
    if not pais:
        print("Por favor, ingrese un pais")
    
    # actualizamos datos
    encontrado = False
    for item in paises:
        if pais in item['nombre']:
            encontrado = True
            print(f"Pais: {item['nombre']} - Poblacion: {item['poblacion']} - Superficie: {item['superficie']} - Continente: {item['continente']}")

            
    if not encontrado:
        print("No se encuentra el pais en la lista\n")

# Mostrar lista
def mostrar_lista():
    mostrar_submenu_listado()

# Ordenar paises
def ordenar_paises():
    mostrar_submenu_ordenamiento()

# Mostrar estadistica
def mostrar_estadistica():
    mostrar_submenu_estadistica()




# Funciones sub menu

# Mostrar submenu actualizar
def mostrar_submenu_actualizar():
    while True:

        for seleccion in sub_menu_actualizar:
            print(seleccion)
        
        # Ingreso de opcion por parte de usuario
        print()
        opcion = input("Ingrese una opción válida: ").strip()

        print("------------------------------------------------")
        print()

        match opcion:
            case '1':
                actualizar_poblacion()
            case '2':
                actualizar_superficie()
            case '3':
                break
            case _:
                print("Opción no válida")



# Mostrar submenu listado
def mostrar_submenu_listado():
     while True:
        print()
        for seleccion in sub_menu_listado:
            print(seleccion)
        
        # Ingreso de opcion por parte de usuario
        print()
        opcion = input("Ingrese una opción válida: ").strip()

        print("------------------------------------------------")
        print()

        match opcion:
            case '1':
                mostrar_lista_completa()
            case '2':
                filtrar_continente()
            case '3':
                rango_poblacion()
            case '4':
                rango_superficie()
            case '5':
                break
            case _:
                print("Opción no válida")

# Mostrar submenu ordenamiento
def mostrar_submenu_ordenamiento():
    while True:

        for seleccion in sub_menu_ordenamiento:
            print(seleccion)
        
        # Ingreso de opcion por parte de usuario
        print()
        opcion = input("Ingrese una opción válida: ").strip()

        print("------------------------------------------------")
        print()

        match opcion:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                break
            case _:
                print("Opción no válida")

# Mostrar submenu estadistica
def mostrar_submenu_estadistica():
    while True:

        for seleccion in sub_menu_estadisticas:
            print(seleccion)
        
        # Ingreso de opcion por parte de usuario
        print()
        opcion = input("Ingrese una opción válida: ").strip()

        print("------------------------------------------------")
        print()

        match opcion:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                break
            case _:
                print("Opción no válida")


# Muestra el menu
def mostrar_menu():
    while True:
        print()
        print("---Gestor de datos de paises---")
        print()
        # Imprime el menu
        for seleccion in menu:
            print(seleccion)
        
        # Ingreso de opcion por parte de usuario
        print()
        opcion = input("Ingrese una opción válida: ").strip()

        print("------------------------------------------------")
        print()

        # Opciones del menu principal
        match opcion:
            case '1':
                agregar_pais()
                
            case '2':
                actualizar_datos()
                
            case '3':
                buscar_pais()
                
            case '4':
                mostrar_lista()
                
            case '5':
                ordenar_paises()
                
            case '6':
                mostrar_estadistica()
                
            case '7':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida")


# Programa principal
mostrar_menu()