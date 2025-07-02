import random

# Lista de palabras para el juego
palabras = ['python', 'logica', 'programacion', 'datos', 'funciones']

# Selecciona una palabra al azar
palabra_secreta = random.choice(palabras)

# Variables iniciales
intentos = 6
letras_adivinadas = []

# Función para mostrar el progreso actual del jugador
def mostrar_palabra(palabra, letras):
    resultado = ''
    for letra in palabra:
        if letra in letras:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado.strip()

# Función que verifica si el jugador ha ganado
def ha_ganado(palabra, letras):
    for letra in palabra:
        if letra not in letras:
            return False
    return True

# Bucle principal del juego
while intentos > 0:
    print("\nPalabra: ", mostrar_palabra(palabra_secreta, letras_adivinadas))
    print("Intentos restantes:", intentos)

    letra_usuario = input("Ingresa una letra: ").lower()

    # Validación sencilla
    if len(letra_usuario) != 1 or not letra_usuario.isalpha():
        print("Ingresa una única letra válida.")
        continue

    # Letra repetida
    if letra_usuario in letras_adivinadas:
        print("Ya has ingresado esa letra. Intenta otra.")
        continue

    letras_adivinadas.append(letra_usuario)

    # Letra correcta o incorrecta
    if letra_usuario in palabra_secreta:
        print("¡Bien hecho! Letra correcta.")
    else:
        intentos -= 1
        print("Letra incorrecta.")

    # Verificar condición de victoria
    if ha_ganado(palabra_secreta, letras_adivinadas):
        print("\n¡Felicidades, has ganado! La palabra era:", palabra_secreta)
        input("Presione enter para salir")
        break

# Si el jugador perdió
if intentos == 0:
    print("\nHas perdido. La palabra secreta era:", palabra_secreta)
    input("Presione enter para salir")
