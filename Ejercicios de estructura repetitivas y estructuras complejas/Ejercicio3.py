mujeres = 0
varones = 0
mayoresEdad = 0
menoresEdad = 0

for i in range(15):
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona (M/F): ")

    if sexo == "F":
        mujeres += 1
    else:
        varones += 1

    if edad >= 18:
        mayoresEdad += 1
    else:
        menoresEdad += 1

print("Cantidad de mujeres:", mujeres)
print("Cantidad de varones:", varones)
print("Mayores de edad:", mayoresEdad)
print("Menores de edad:", menoresEdad)
