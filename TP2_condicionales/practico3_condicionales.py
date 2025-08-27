# Ejercicios del practico 3

#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
   print("Es mayor de edad")

#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad1 = int(input("Ingrese su edad: "))
if edad1 < 12:
    print("Usted es un/a niño/a")
elif edad1 >= 12 and edad1 < 18:
    print("Usted es un/a adolecente")
elif edad1 >= 18 and edad1 < 30:
    print("Usted es un/a adulto/a joven")
else:
    print("Usted es un/a adulto/a")

#Ejercicio 5
contraseña = input("Ingrese una contraseña (debe tener entre 8 y 14 caracteres): ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and media == moda and mediana == moda:
    print("No hay sesgo")
else:
    print("No entra en ninguna categoria")

# Ejercicio 7
frase = input("Ingrese una frase: ")
VOCALES = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if frase[-1] in VOCALES:
    print(f"{frase}!")
else:
    print(frase)

# Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("""Ingrese una opcion
                   1- Si quiere su nombre en mayúsculas
                   2- Si quiere su nombre en minúsculas
                   3- Si quiere su nombre con la primera letra mayúscula
                   :  """))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingrese una opcion valida")

# Ejercicio 9
terremoto = int(input("Ingrese la magnitud del terremoto: "))
if terremoto < 3:   
    print("'muy leve'(imperceptible)") 
elif terremoto == 3:
    print("'Leve' (ligeramente perceptible)")
elif terremoto == 4:
    print("'Moderado' (sentido por personas, pero generalmente no causa daños)")
elif terremoto == 5:
    print("'Fuerte' (puede causar daños en estructuras débiles)")
elif terremoto == 6:
    print("'Muy Fuerte' (puede causar daños significativos)")
else:
    print("'Extremo' (puede causar graves daños a gran escala)")

# Ejercicio 10
dia = int(input("Ingrese el dia:"))
mes = input("Ingrese el mes:").lower()
hemisferio = input("Ingrese el hemisferio en el que se encuentra(N/S): ").lower()
if (dia >= 21 and mes == 'diciembre') or (dia <= 20 and mes == 'marzo'):
    if hemisferio == 'n':
        print("Es invierno")
    else:
        print("Es verano")
elif mes == 'enero' or mes == 'febrero':
    if hemisferio == 'n':
        print("Es invierno")
    else:
        print("Es verano")
elif (dia >= 21 and mes == 'marzo') or (dia <= 20 and mes == 'junio'):
    if hemisferio == 'n':
        print("Es primavera")
    else:
        print("Es otoño")
elif mes == 'abril' or mes == 'mayo':
    if hemisferio == 'n':
        print("Es primavera")
    else:
        print("Es otoño")
elif (dia >= 21 and mes == 'junio') or (dia <= 20 and mes == 'septiembre'):
    if hemisferio == 'n':
        print("Es verano")
    else:
        print("Es invierno")
elif mes == 'julio' or mes == 'agosto':
    if hemisferio == 'n':
        print("Es verano")
    else:
        print("Es invierno")
else:
    if hemisferio == 'n':
        print("Es otoño")
    else:
        print("Es primavera")