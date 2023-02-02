import matplotlib.pyplot as plt

#Este programa imprime por pantalla la sucesión de fibonacci, de los n numeros que el usuario desee
#Además imprime un gráfico mostrando dicha sucesión

print("## Sucesion de Fibonacci ##")

#CONSTANTES
n = int(input("     Ingrese un numero para calcular la sucesion de fibonacci: "))

#FUNCIONES
#Funcion que crea una lista de numeros con orden ascendente de 0 hasta "largo"
def numeroAscendente(lista,largo):
    i = 0
    while(i<largo):
        lista.append(i+1)
        i = i+1

#Fibonacci Iterativo
def fibonacci(n, lista):
    lista.append(1)
    lista.append(1)
    a = lista[0]
    b = lista[1]
    c = 0
    i = 2
    while(i<n):
        lista.append(a+b)
        a = b
        b = lista[i]
        i = i+1
    return lista[i-1]
        

#MAIN
lista_x = []
lista_y = []
numeroFibonacci = fibonacci(n, lista_x)
numeroAscendente(lista_y, n)
print("     El resultado de la sucesion de Fibonacci es:",numeroFibonacci)
print("     Sucesión de Fibonacci hasta", n,":")
print("    ",lista_x)

plt.plot(lista_x, lista_y)
plt.show()