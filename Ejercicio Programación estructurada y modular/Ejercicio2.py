
def saludo(mensaje, nombre, respuesta):
    print("hola " + nombre + ", ¿Qué tal?")
    

nombre = ["Ana", "Juan", "Matías"]
i = 0

while i < len(nombre):
    print("----------------")
    saludo(mensaje, nombre[i],)
    print()
    i += 1