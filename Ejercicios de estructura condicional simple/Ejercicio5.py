pesos = float(input("Ingrese la cantidad de pesos o dolares que desee convertir: "));
tipo_cambio = input("Ingrese el tipo de cambio (dolares a pesos o pesos a dolares): ");
dolar_hoy = float(input("Ingrese el valor de 1 pesos a dolar al día de hoy:"));
pesos_hoy  = float(input("Ingrese el valor de 1 dolar a pesos al día de hoy:"));

if tipo_cambio == "dolares a pesos":
    dolares = pesos / dolar_hoy
    print("El equivalente en dólares es:", dolares)
elif tipo_cambio == "pesos a dolares":
    pesos_arg = pesos * pesos_hoy
    print("El equivalente en pesos es:", pesos_arg)
else:
    print("Tipo de cambio no válido")