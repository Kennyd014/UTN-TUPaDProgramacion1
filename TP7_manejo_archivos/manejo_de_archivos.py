import os

# Ejercicio 1

# Creamos la lista que ira en el archivo.txt
productos = [
"Nombre,Precio,Cantidad\n",
"Camisas,25.50,15\n",
"Remeras,20.0,20\n",
"Pantalones,27.5,10\n"
]


# agregamos la lista al archvo y lo creamos
if not os.path.exists("productos.txt"):

    with open("productos.txt", "a") as archivo:
        archivo.writelines(productos)

productos_diccionario = []


# Ejercicio 2
# recorremos la lista, y lo leemos desde la posicion 1 para saltear los titulos
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        if partes[0].lower() == 'nombre':
            continue
        #asignamos los datos a un diccionario
        nombre,precio,cantidad = partes
        
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")


# Ejercicio 3
producto_nombre = input("Ingrese el nombre del producto a agregar: ")
producto_precio = float(input("Ingrese el precio del producto a agregar: "))
producto_cantidad = int(input("Ingrese la cantidad del producto nuevo al stock: "))

with open("productos.txt", "a") as archivo:
    archivo.write(f"{producto_nombre},{producto_precio},{producto_cantidad}\n")


# Ejercicio 4, cargar productos en una lista de diccionarios

with open("productos.txt","r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        if partes[0].lower() == 'nombre':
            continue
        #asignamos los datos a un diccionario
        nombre,precio,cantidad = partes
        #nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            'nombre': nombre,
            'precio': float(precio),
            'cantidad': int(cantidad)
        }
        productos_diccionario.append(producto)

print(productos_diccionario)



# Ejercicio 5, buscar un producto por nombre

buscar_producto = input("Ingrese el nombre del producto que desea buscar: ")
encontrado = False

for producto in productos_diccionario:
    if producto['nombre'].lower() == buscar_producto.strip().lower():
        print(f"Producto encontrado {producto}")
        encontrado = True
        break
    
if not encontrado:
    print("Producto no encontrado")

# Ejercicio 6, guardar los datos actualizados

with open("productos.txt", "w") as archivo:
    for producto in productos_diccionario:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")