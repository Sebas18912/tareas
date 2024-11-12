# Programa para determinar el mayor de tres números

# Función para encontrar el mayor de tres números
def mayor_de_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Solicitar al usuario que ingrese los números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

# Llamar a la función y mostrar el resultado
mayor = mayor_de_tres(numero1, numero2, numero3)
print("El mayor de los tres números es:", mayor)
