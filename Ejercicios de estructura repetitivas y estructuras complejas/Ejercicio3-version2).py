mujeres = 0
varones = 0
mayores_edad = 0
menores_edad = 0

for i in range(15):
    try:
        edad = int(input("Ingrese la edad de la persona: "))
    except ValueError:
        print("El dato ingresado no es correcto. Ingrese un valor numérico.")
        continue

    sexo = input("Ingrese el sexo de la persona (F/M): ")

    if sexo.upper() == "F":
        mujeres += 1
    elif sexo.upper() == "M":
        varones += 1
    else:
        print("Sexo no válido. Por favor, ingrese 'F' o 'M'.")
        continue

    if edad >= 18:
        mayores_edad += 1
    else:
        menores_edad += 1

print("Cantidad de mujeres:", mujeres)
print("Cantidad de varones:", varones)
print("Cantidad de personas mayores de edad:", mayores_edad)
print("Cantidad de personas menores de edad:", menores_edad)
