meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

numero = int(input("Ingrese un número del 1 al 12: "))

if 1 <= numero <= 12:
    print(meses[numero - 1])
else:
    print("Número inválido. Por favor, ingrese un número del 1 al 12.")
