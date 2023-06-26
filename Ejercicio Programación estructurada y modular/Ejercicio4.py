def comparar_numeros(num1, num2):
    if num1 == num2:
        resultado = True
    else:
        resultado = False
    return resultado

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

es_igual = comparar_numeros(numero1, numero2)
print(es_igual)
