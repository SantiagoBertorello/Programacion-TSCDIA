
def intercambiar_respuesta(mensaje, aula, respuesta):
    print(mensaje + aula + ", ¿Qué tal?")
    print(respuesta)

aulas = ["101", "202", "303"]
i = 0
mensaje = "Hola Aula "
respuestas = ["Andamos bien, gracias por preguntar.", "Hola, buen día!", "Hay días mejores..."]

while i < len(aulas):
    print("----------------")
    intercambiar_respuesta(mensaje, aulas[i], respuestas[i])
    print()
    i += 1