numeros = []
pares = 0
impares = 0
suma_pares = 0

for i in range(4):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
        suma_pares += numero
    else:
        impares += 1

print("La cantidad de números pares es", pares)
print("La cantidad de números impares es", impares)
print("La Sumatoria de los números pares es", suma_pares)
