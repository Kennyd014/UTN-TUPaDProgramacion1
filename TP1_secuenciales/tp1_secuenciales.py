# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# Ejercicio 3
nombre1 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarResidencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre1} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")

# Ejercicio 4
radio = int(input("Ingrese el radio del circulo: "))
pi = 3.14159265359
area = pi *(radio * radio)
perimetro = 2 * pi * radio
print(f"El area es de: {area} cm, y el perimetro es de: {perimetro} cm.")

# Ejercicio 5
segundos = int(input("Ingrese los segundos: "))
segundosEnHora = 3600
totalHoras = segundos / segundosEnHora
print(f"La cantidad de segundos ingresada equivale a: {totalHoras} horas")

# Ejercicio 6
multiplicador = int(input("Ingrese un numero: "))
for i in range(1,100,1):
    resultado = multiplicador * i
    print(resultado)

# Ejercicio 7
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 == 0 or num2 == 0:
    print("Ingrese numeros enteros distintos a 0.")
else:
    suma = num1 + num2
    resta = num1 - num2
    division = num1 / num2
    multiplicacion = num1 * num2
    print(f"El resultado de la suma es: {suma}, el resultado de la resta es: {resta}, el resultado de la  division es: {division} y el resultado de la multiplicacion es de: {multiplicacion}")

# Ejercicio 8
altura = float(input("Ingrese su altura en cm(Ej: 1.80): "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura * altura)
print(f"Su IMC es de: {imc}")

# Ejercicio 9
temperaturaCelsius = int(input("Ingrese la temperatura en grados Celsius: "))
celciusAFahrenheit = (9/5) * temperaturaCelsius + 32
print(f"La temperatura es de {celciusAFahrenheit} grados fahrenheit")

# Ejercicio 10
num1Prom = int(input("Ingrese el primer numero: "))
num2Prom = int(input("Ingrese el segundo numero: "))
num3Prom = int(input("Ingrese el tercer numero: "))
promedio = (num1Prom + num2Prom + num3Prom) / 3
print(f"El promedio es de: {promedio}")