from collections import Counter

ruta = r"C:\Users\Santiago\Documents\Santiago\Estudio\Universidad\UNAL\Segundo semestre\Programación Básica\Archivo Reto 11.txt"

with open(ruta, "r", encoding="utf-8") as archivo:
    contenido = archivo.read().lower()  # Leer y convertir a minúsculas

    # Contar vocales incluyendo tildes
    vocales = {
        "a": contenido.count("a") + contenido.count("á"),
        "e": contenido.count("e") + contenido.count("é"),
        "i": contenido.count("i") + contenido.count("í"),
        "o": contenido.count("o") + contenido.count("ó"),
        "u": contenido.count("u") + contenido.count("ú") + contenido.count("ü")
    }

    # Contar consonantes
    consonantes = sum(1 for c in contenido if c.isalpha() and c not in "aeiouáéíóúü")

    # Obtener palabras sin regex
    palabras = [p.strip(".,;:!?¿¡()[]{}\"'") for p in contenido.split() if p.strip(".,;:!?¿¡()[]{}\"'").isalpha()]

    # Contar las 50 palabras más comunes
    palabras_comunes = Counter(palabras).most_common(50)

# 📌 Mostrar resultados
print(f"Número de vocales (incluyendo tildes): {vocales}")
print(f"Cantidad de consonantes: {consonantes}\n")
print("Las 50 palabras más repetidas:")
for palabra, frecuencia in palabras_comunes:
    print(f"{palabra}: {frecuencia}")

