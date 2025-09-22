# Solicitar N cantidad de Números y al momento de imprimir separarlos por pares e impares.

cantidadNumeros = int(input("Ingresa la cantidad de numeros  a separar: "))

pares = []
impares = []

for i in range (0, cantidadNumeros):
    numero = int(input("Ingresa número: "))
    if(numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)
print("Números par: ")

print(pares)

print("Números impar: ")

print(impares)