import csv
import os

NOMBRE_ARCHIVO = "catalogo.csv"
# Listas
menu = [  "1. Ingresar títulos",
          "2. Ingresar ejemplares",
          "3. Mostrar catálogo",
          "4. Consultar disponibilidad",
          "5. Listar agotados",
          "6. Agregar título",
          "7. Actualizar ejemplares (préstamo/devolución)",
          "8. Salir"
          ]



# Funciones auxiliares

# Obtener catalogo, abre un archivo csv, lo recorre y devuelve la lista titulos
def obtener_catalogo():
    titulos = []

    # Si el archivo no existe, lo crea, con los campos de titulo y de cantidad
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'w', newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["titulo","cantidad"])
            escritor.writeheader()
            return titulos
        
    # Si el archivo ya existe, lo muestra    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            titulos.append({"titulo": fila["titulo"], "cantidad": int(fila["cantidad"])})
    return titulos

# Agregar titulo
def agregar_titulo(nuevo_titulo):
    with open(NOMBRE_ARCHIVO, 'a', newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["titulo","cantidad"])
        escritor.writerow(nuevo_titulo)

# Guardar item
def guardar_item(titulos):
    with open(NOMBRE_ARCHIVO, 'w', newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["titulo","cantidad"])
        escritor.writeheader()
        escritor.writerows(titulos)

# Validaciones

# Verificar si ya existe el titulo
def existe_titulo(nuevo_titulo):
    titulos = obtener_catalogo()

    for titulo in titulos:
        if titulo["titulo"].lower() == nuevo_titulo.strip().lower():
            return True
    
    return False

# Validar titulo vacio
def validar_vacio(nuevo_titulo):
    if nuevo_titulo == "":
        return False
    
    return True

# Validar cantidad
def validar_numero(cantidad):
    if not cantidad.isdigit():
        return False
    
    return True
    
#Validacion lista vacia
def validar_catalogo():
    titulos = obtener_catalogo()
    if not titulos:
        print("Aún no hay títulos ingresados. Por favor, ingrese un título primero para luego poder agregar el número de ejemplares")






# Funciones de menu

# Ingresar titulos
def ingresar_titulos():
    print("---Ingresar Titulo---")
    nuevo_titulo = input("Ingrese el nuevo título: ").upper().strip()

    if existe_titulo(nuevo_titulo):
        print("El titulo ya existe")
        return
    
    # Validar vacio
    if not validar_vacio(nuevo_titulo):
        print("El titulo ingresado no es valido")
        return

    cantidad = input("Ingrese la cantidad de ejemplares: ").strip()
    
    # Validad cantidad
    if not validar_numero(cantidad):
        print("La cantidad ingresada no es valida")
        return
    
    cantidad = int(cantidad)


    # Funcion para agregar el producto
    agregar_titulo({'titulo': nuevo_titulo, 'cantidad': cantidad})
    print("Se agrego correctamente el nuevo titulo")

    

# Ingresar ejemplares
def ingresar_ejemplares():
    titulos = obtener_catalogo()

    # Validar lista vacia
    validar_catalogo()

    titulo_input = input("Ingrese el titulo al que desea agregarle ajemplares: ").strip()
    
    # Validacion de titulo vacio
    if not titulo_input:
        print("Por favor, ingrese un titulo")
    
    for item in titulos:
        if item["titulo"].lower() == titulo_input.lower():
            cantidad = input("Ingrese la cantidad a agregar: ").strip()

            if not validar_numero(cantidad):
                print("La cantidad no es valida")
                return
            
            cantidad = int(cantidad)
            item["cantidad"] += cantidad
            guardar_item(titulos)
           
            print(f"Se agrego correctamente la cantidad de {cantidad} al titulo {item['titulo']}, el total ahora es de: {item['cantidad']}")       
            return 

            
    else:    
        print("No se encontro el titulo")
        

# Mostrar catalogo
def mostrar_catalogo():
    titulos = obtener_catalogo()

    # Validacion de lista vacia
    validar_catalogo()

    print("---Catalogo---")    
    for titulo in titulos:
        print(f"TITULO: {titulo["titulo"]} - CANTIDAD: {titulo["cantidad"]}")
        
        

# Consultar disponibilidad
def consultar_disponibilidad():
    pass

# Listar agotados
def listar_agotados():
    pass

# Agregar titulo
#def agregar_titulo():
 #   pass

# Actualizar ejemplares
def actualizar_ejemplares():
    pass

# Muestra el menu
def mostrar_menu():
    while True:
        print()
        print("---Menú Biblioteca---")

        for seleccion in menu:
            print(seleccion)
        
        # Ingreso de opcion del menu por parte del usuario
        print()
        opcion = input("Ingrese una opción válida: ").strip()
        
        print("----------------------------------------------")   
        print()
        # Opciones en el Menu
        match opcion:
            case "1": 
                ingresar_titulos()
                
            case "2": 
                ingresar_ejemplares()
                
            case "3": 
                mostrar_catalogo()
                
            case "4":
                consultar_disponibilidad() 
                pass
            case "5":
                listar_agotados() 
                pass
            case "6": 
                #agregar_titulo()
                pass
            case "7": 
                actualizar_ejemplares()
                pass
            case "8": 
                break
            case _:
                print("Opción no válida")

mostrar_menu()