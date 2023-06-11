# Por lo aprendido en un curso de Javascript(muy básico), enseñaba que el programa tire números aleatorios. Con esta idea, busque en el material complementario como hacer esta misma funcion con python. También, cambie la funcion de range por la de while.

import random

numeros = []
pares = 0
impares = 0
suma_pares = 0

contador = 0
while contador < 4:
    numero = random.randint(1, 200)  
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
        suma_pares += numero
    else:
        impares += 1
    contador += 1

print("Números generados aleatoriamente:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("suma de los números pares:", suma_pares)

