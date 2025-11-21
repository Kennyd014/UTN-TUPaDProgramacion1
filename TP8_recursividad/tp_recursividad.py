
# Ejercicio 1 - Factorial
# Funcion para obtener el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Input del usuario
numero = int(input("Ingrese un numero: "))
# Bucle para recorrer todos los numeros y mostrar el factorial de cada uno
for i in range(1, numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")

# Ejercicio 2 - Fibonacci
# Funcion fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input del usuario    
posicion = int(input("Ingrese la posicion elegida: "))

# Bucle para mostrar resultados hasta esa posicions
for i in range(posicion + 1):
    print(fibonacci(i))


# Ejercicio 3 - potencia de un n

# Funcion potencia
def potencia(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
# Algoritmo
def algoritmo():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = potencia(base,exponente)
    print(f"{base} potencia de {exponente} es: {resultado}")

# Ejecucion
algoritmo()


# Ejercicio 4 - Binario
# conversion a binario
def binario(n):
    if n == 0:
        return ""
    else:
        return binario(n // 2) + str(n % 2)
    
# Input del usuario
def main():
    numero = int(input("ingrese un numero positivo: "))
    if numero == 0:
        print("0")
    elif numero < 0:
        print("El numero debe ser positivo y mayor a 0")
    else:
        num_binario = binario(numero)
        print(f"El binario de {numero} es: {num_binario}")

# Ejecucion
main()



# Ejercicio 5 - es palindromo
# recursiva
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# input de usuario
palabra = input("Ingrese una palabra: ")

print(es_palindromo(palabra))


# Ejercicio 6 - Suma digitos
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
print(suma_digitos(54565)) 


# Ejercicio 7 - contar bloques
def contar_boques(n):
    if n == 0:
        return 0
    else:
        return n + contar_boques(n - 1)

print(contar_boques(4))


# Ejercicio 8 - Contar digito
def contar_digito(numero,digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

print(contar_digito(1341234,2))