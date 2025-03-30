import random

def generar_historia():
    heroes = ["Captain Awesome", "Nacho Cheese Man", "Turbo el Hámster"]
    villanos = ["Queen Stinkypants", "Dr. Slime", "El Monstruo Come Juguetes"]
    problemas = [
        "ha robado todos los lápices de colores de la escuela",
        "ha escondido todos los videojuegos en una cueva secreta",
        "ha lanzado un hechizo que convierte las matemáticas en trabalenguas"
    ]
    soluciones = [
        "usaron su súper inteligencia para resolver el misterio",
        "crearon una trampa de queso pegajoso para atrapar al villano",
        "convencieron al villano de que jugar limpio es más divertido"
    ]
    
    heroe = random.choice(heroes)
    villano = random.choice(villanos)
    problema = random.choice(problemas)
    solucion = random.choice(soluciones)
    
    historia = f"Un día, {heroe} descubrió que {villano} {problema}. ¡Era un desastre total! Pero con ingenio y valentía, {heroe} y su equipo {solucion}. ¡La ciudad está a salvo otra vez!"
    return historia

# Generar una historia aleatoria
print(generar_historia())
