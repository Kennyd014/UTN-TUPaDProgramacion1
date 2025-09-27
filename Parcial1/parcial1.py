

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
titulos = []
ejemplares = []


# Variables
nuevo_titulo = ""
indice_titulos = 0
cantidad_ejemplares = 0 
buscar_titulo = ""
encontrado = False

opcion_menu_7 = ""
cantidad_prestada_retornada = 0
opcion = 0
salir = False

# Validacion de mayusculas y minusculas en los titulos
for titulo in titulos:
    titulo = titulo.upper()
    titulos.append(titulo)

# Programa 
while salir == False:
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

            nuevo_titulo = input("Ingrese el nuevo título: ").upper()
            while nuevo_titulo in titulos or nuevo_titulo == "":
                print("Ese título ya está en el catálogo o no se ingresó correctamente. Por favor, intente nuevamente")
                nuevo_titulo = input("Ingrese el nuevo título: ").upper()
            
            print(F"Título {nuevo_titulo} ingresado correctamente")
            titulos.append(nuevo_titulo)
            indice_titulos = titulos.index(nuevo_titulo)
            ejemplares.insert(indice_titulos, 0)

        case "2":

            # Validacion de lista vacia
            if not titulos:
                print("Aún no hay títulos ingresados. Por favor, ingrese un título primero para luego poder agregar el número de ejemplares")
                continue

            for i, titulo in enumerate(titulos):
                print(f"{i + 1} - {titulo}")
            
            indice_titulos = int(input("Seleccione el índice del título a ingresar: ")) -1

            while indice_titulos < 0 or indice_titulos >= len(titulos):
                print("Índice inválido. Por favor, intente nuevamente")
                indice_titulos = int(input("Seleccione el índice del título a ingresar: ")) -1

            cantidad_ejemplares = int(input("Ingrese la cantidad de ejemplares: "))
            ejemplares[indice_titulos] += cantidad_ejemplares
            print(F"Los ejemplares disponibles para {titulos[indice_titulos]} son {ejemplares[indice_titulos]}")
            
        case "3":

            # Validacion de lista vacia
            if not titulos:
                print("Aún no hay títulos ingresados. Por favor, ingrese un título primero para luego poder agregar el número de ejemplares")
                continue
            print("---Catálogo de Libros---")

            for titulo in range(len(titulos)):
                print(f"Título : {titulos[titulo]} - Ejemplares: {ejemplares[titulo]}") 

        case "4":

            if not titulos:
                print("Aún no hay títulos ingresados. Por favor, ingrese un título primero para luego poder agregar el número de ejemplares")
                continue
            buscar_titulo = input("Ingrese el título requerido: ").upper()
            encontrado = False

            while True:
                if buscar_titulo in titulos:
                    indice_titulos = titulos.index(buscar_titulo)
                    print(f"Título {buscar_titulo} encontrado, hay {ejemplares[indice_titulos]} copias en stock")
                    break
                else:
                    print("No poseemos ese título en nuestro catálogo, desea intentar con otro título? (Si/No)")  
                    if input().upper() == "SI":
                        buscar_titulo = input("Ingrese el título requerido: ").upper()
                    else:
                        break

        case "5":

            if not titulos:
                print("Aún no hay títulos ingresados. Por favor, ingrese un título primero para luego poder agregar el número de ejemplares")
                continue
            
            agotados = False

            for i in ejemplares:
                if i == 0:
                    agotados = True
                    break
            
            if agotados:
                print("---Libros Agotados---")
                for titulo in titulos:
                    indice_titulos = titulos.index(titulo)
                    if ejemplares[indice_titulos] == 0:
                        print(titulo)
                    
        case "6":

            nuevo_titulo = input("Ingrese el nuevo título: ").upper()
            while nuevo_titulo in titulos or nuevo_titulo == "":
                print("Ese título ya esta en el catálogo o no se ingreso correctamente, por favor intente nuevamente")
                nuevo_titulo = input("Ingrese el nuevo título: ").upper()

            titulos.append(nuevo_titulo)
            cantidad_ejemplares = int(input("Ingresar la cantidad de ejemplares para ese título: "))
            indice_titulos = titulos.index(nuevo_titulo)
            ejemplares.insert(indice_titulos, cantidad_ejemplares)
            print(F"Título {nuevo_titulo} con {cantidad_ejemplares} ejemplares ingresado correctamente")

        case "7":

            if not titulos:
                print("Aún no hay títulos ingresados. Por favor, ingrese un título primero para luego poder agregar el número de ejemplares")
                continue
            
            opcion_menu_7 = input('Ingrese "Prestamo" si fue prestado un título, o "Devolucion" si fue devuelto un título: ')
            opcion_menu_7 = opcion_menu_7.upper()
            
            if opcion_menu_7 == "PRESTAMO" or opcion_menu_7 == "DEVOLUCION":
                #for i in range(len(titulos)):
                 #   print(i, titulos[i])
                for i, titulo in enumerate(titulos):
                    print(f"{i + 1} - {titulo}")
                if opcion_menu_7 == "PRESTAMO":

                    indice_titulos = int(input("Seleccione el índice del título: "))
                    while indice_titulos < 1 or indice_titulos > len(titulos):
                        print("Índice incorrecto, intente nuevamente")
                        indice_titulos = int(input("Seleccione el índice del título: "))

                    cantidad_prestada_retornada = int(input("Ingrese la cantidad de ejemplares prestados de dicho título: "))
                    if ejemplares[indice_titulos - 1] < cantidad_prestada_retornada:
                        print("No se puede realizar la solicitud por falta de stock")
                    else:
                        ejemplares[indice_titulos - 1] = ejemplares[indice_titulos - 1] - cantidad_prestada_retornada
                    print(f"Se han prestado {cantidad_prestada_retornada} ejemplares del título {titulos[indice_titulos - 1]} del stock")
                elif opcion_menu_7 == "DEVOLUCION":

                    indice_titulos = int(input("Seleccione el índice del título: "))
                    while indice_titulos < 1 or indice_titulos > len(titulos):
                        print("Índice incorrecto, intente nuevamente")
                        indice_titulos = int(input("Seleccione el índice del título: "))
                    cantidad_prestada_retornada = int(input("Ingrese la cantidad de ejemplares devueltos de dicho título: "))
                    ejemplares[indice_titulos - 1] = ejemplares[indice_titulos - 1] + cantidad_prestada_retornada
                    print(f"Se han devuelto {cantidad_prestada_retornada} ejemplares del título {titulos[indice_titulos - 1]} al stock")
            else:
                print("Opción no válida")
            
        case "8":
            salir = True
            print("Saliendo del programa...")
            
        case _:
            print("Opción no válida")


