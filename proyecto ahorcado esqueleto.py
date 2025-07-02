import random

# Definir los datos iniciales
palabras = ['python', 'logica', 'programacion']
palabra_secreta = random.choice(palabras)
letras_adivinadas = [] 
intentos = 6

print("¡Bienvenido al Juego del Ahorcado!")
# Pista probar si muestra la palabra
print(f"(La palabra es: {palabra_secreta})") # Ayuda para probar
