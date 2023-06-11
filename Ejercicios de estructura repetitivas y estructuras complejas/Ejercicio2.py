numeros = []

for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

mayores = 0
menores = 0
maximo = numeros[0]
minimo = numeros[0]

for numero in numeros:
    if numero > 100:
        mayores += 1
    else:
        menores += 1

    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero

print("Números mayores a 100:", mayores)
print("Números menores a 100:", menores)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)