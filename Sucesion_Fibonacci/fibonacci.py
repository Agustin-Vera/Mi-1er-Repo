#Este programa imprime por pantalla la sucesion de fibonacci, de los n numeros que el usuario desee

print("Este programa calcula el valor de la sucesion de Fibonacci")

#CONSTANTES
n = int(input("     Ingrese un numero para calcular la sucesion de fibonacci: "))

#FUNCIONES
#Fibonacci recursivo
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Main
numeroFibonacci = fibonacci(n)

print("     El resultado de la sucesion de fibonacci hasta",n,"es:",numeroFibonacci)