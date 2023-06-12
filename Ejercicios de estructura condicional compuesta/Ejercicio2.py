importe = float(input("Ingrese el importe: "))
forma_pago = int(input("Ingrese la forma de pago (1: Contado, 2: Tarjeta de Crédito, 3: QR, 4 Débito): "))

if forma_pago == 1:
    descuento = importe * 0.10
    importe_total = importe - descuento
    print("Importe:", importe)
    print("Descuento:", descuento)
    print("Importe total:", importe_total)
elif forma_pago == 2:
    interes = importe * 0.10
    importe_total = importe + interes
    print("Importe:", importe)
    print("Interés:", interes)
    print("Importe total:", importe_total)
elif forma_pago = 3;
    interes = importe * 0.9
    importe_total = importe + interes
    print("Importe:", importe)
    print("Interés:", interes)
    print("Importe total:", importe_total)    
elif forma_pago == 4:
    descuento = importe * 0.05
    importe_total = importe - descuento
    print("Importe:", importe)
    print("Descuento:", descuento)
    print("Importe total:", importe_total)
else:
    print("Forma de pago inválida. Por favor, ingrese 1, 2 o 3.")
