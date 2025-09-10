import random
# Ejercicio 1

for n in range(100+1):
    print(n)

# Ejercicio 2

num = input("ingrese un numero: ")
contador = 0
for n in num:
    contador = contador + 1
print(f"El numero ingresado tiene: {contador} cifras")

# Ejercicio 3 

num1 = int(input("Ingrese el primer valor: ") )
num2 = int(input("Ingrese el segundo valor: "))
suma = 0
for n in range(num1 + 1, num2):
    suma = suma + n
print(suma)

# Ejercicio 4

suma2 = 0
salir = True
while salir:
    num3 = int(input("Ingrese un numero entero: "))
    suma2 = suma2 + num3
    if num3 == 0:
        salir = False
print(f"El total de la suma es de: {suma2}")

# Ejercicio 5

player1 = 10
intentos = 0
num_aleatorio = 100
while player1 != num_aleatorio:
    player1 = int(input("Ingrese un numero del 0 al 9: "))
    num_aleatorio = random.randint(0,9)
    intentos += 1
print(f"Felicidades, el numero era {num_aleatorio} y lo adivinaste en {intentos} intentos")

# Ejercicio 6

for n in range(100,-1, -1):
    if n % 2 == 0:
        print(n) 

# Ejercicio 7

num4 = int(input("Ingrese el segundo valor: "))
suma3 = 0
for n in range(0, num4 + 1):
    suma3 = suma3 + n
print(suma3)

# Ejercicio 8

tot_par = 0
tot_impar = 0
tot_neg = 0
tot_pos = 0
for n in range(0, 100):
    num5 = int(input("ingrese un numero entero: "))
    if num5 % 2 == 0:
        tot_par += 1
        if num5 > 0:
            tot_pos += 1
        else:
            tot_neg +=1
    else:
        tot_impar += 1
        if num5 > 0:
            tot_pos += 1
        else:
            tot_neg +=1
print(f"En total hay {tot_par} numeros pares, {tot_impar} numeros impares, {tot_pos} numeros positivos y {tot_neg} numeros negativos")

    
# Ejercicio 9

total = 0
for n in range(0, 100):
    num6 = int(input("ingrese un numero entero: "))
    total = total + num6
print(f"La media de los numeros es de: {total / 10}")

# Ejercicio 10

numero = input("Ingrese un numero: ")
for n in range(len(numero) - 1, -1, -1):
    print(numero[n])





