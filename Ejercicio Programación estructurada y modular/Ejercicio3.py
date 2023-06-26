import random

def suma1(parametros):
    suma = sum(parametros)
    return suma

parametros = [random.randint(1, 100) for _ in range(3)]
resultado1 = suma1(parametros)
print("El resultado es:", resultado1)


def suma2(parametros):
    suma = sum(parametros)
    return suma

parametros = []
for i in range(3):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    parametros.append(numero)

resultado2 = suma2(parametros)
print("El resultado es:", resultado2)