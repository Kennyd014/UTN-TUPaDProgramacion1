# Funciones

# 1- Imprimir Hola Mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2- Saludar_usuario(nombre)
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# 3- Informacion_personal(nombre,apellido,edad,residencia)
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4- Calcualar_area_circulo(radio) calcular_perimetro_circulo(radio)
def calcular_area_circulo(radio):
    pi = 3.14159
    return pi * (radio * radio)

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    return 2*pi*radio

# 5- Segundos_a_horas(segundos)
def segundos_a_horas(segundos):
    return segundos // 3600

# 6- Tabla_multiplicar(numero)
def table_multiplicar(numero):
   
    for n in range(1,11):
       resultado=  numero * n
       print(f"La tabla de multiplicar del {numero} es: {numero}x{n} = {resultado}")

# 7- Operaciones_basicas(a,b)
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

# 8-Calcular_imc(peso,altura):
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2) 
    return imc

# 9-celsius_a_fahrenheit(celsius)
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 10- Calcular_promedio(a,b,c)
def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    return promedio


# Programa pincipal

# Entradas de tatos del usuario
nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: " )
edad = int(input("Por favor ingrese su edad: "))
residencia = input("Por favor ingrese su residencia: ")
radio = int(input("Ingrese el radio del circulo: "))
segundos = int(input("Ingrese los segundos que desea convertir: "))
numero = int(input("Ingrese el numero a multiplicar: "))
valor1 = int(input("Ingrese el primer valor a operar: "))
valor2 = int(input("Ingrese el segundo valor a operar: "))
peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
prom_1 = int(input("Ingrese el primer numero para el promedio: "))
prom_2 = int(input("Ingrese el segundo numero para el promedio: "))
prom_3 = int(input("Ingrese el tercer numero para el promedio: "))

# Llamadas a funciones

imprimir_hola_mundo()
saludar_usuario(nombre)
informacion_personal(nombre,apellido,edad,residencia)
print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))
print("Equivalen a ",segundos_a_horas(segundos), " Horas")
table_multiplicar(numero)
resultados = operaciones_basicas(valor1,valor2)
print(f"El resultado de la suma es: {resultados[0]}")
print(f"El resultado de la resta es: {resultados[1]}")
print(f"El resultado de la multiplicacion es: {resultados[2]}")
print(f"El resultado de la division es: {resultados[3]}")
print("Su IMC es: ",calcular_imc(peso,altura))
print("La temperatura en grados fahrenheit es de: ",celsius_a_fahrenheit(celsius))
print("El promedio es de: ", calcular_promedio(prom_1,prom_2,prom_3))


