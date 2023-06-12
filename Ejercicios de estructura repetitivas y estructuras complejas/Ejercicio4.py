numeros = []
sumatoria_positivos = 0

for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    if numero > 0:
        sumatoria_positivos += numero

print("Números positivos:", [numero for numero in numeros if numero > 0])
print("Sumatoria de los números positivos:", sumatoria_positivos)
