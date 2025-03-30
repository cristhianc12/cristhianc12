import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Captain Awesome: Atrapa las Estrellas!")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Cargar imágenes
captain = pygame.image.load("captain_awesome.png")  # Asegúrate de tener esta imagen
captain = pygame.transform.scale(captain, (80, 80))

# Posiciones iniciales
player_x, player_y = WIDTH // 2, HEIGHT - 100
player_speed = 10

star = pygame.image.load("star.png")  # Imagen de estrella
star = pygame.transform.scale(star, (40, 40))
star_x = random.randint(0, WIDTH - 40)
star_y = 0
star_speed = 5

# Puntuación y tiempo
score = 0
font = pygame.font.Font(None, 36)
time_left = 30  # Segundos
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Bucle del juego
running = True
while running:
    screen.fill(WHITE)
    
    # Control del tiempo
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_left = max(30 - elapsed_time, 0)
    if time_left == 0:
        running = False
    
    # Eventos del teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 80:
        player_x += player_speed
    
    # Movimiento de la estrella
    star_y += star_speed
    if star_y > HEIGHT:
        star_x = random.randint(0, WIDTH - 40)
        star_y = 0
    
    # Colisión
    if abs(player_x - star_x) < 50 and abs(player_y - star_y) < 50:
        score += 1
        star_x = random.randint(0, WIDTH - 40)
        star_y = 0
    
    # Dibujar en pantalla
    screen.blit(captain, (player_x, player_y))
    screen.blit(star, (star_x, star_y))
    score_text = font.render(f"Puntos: {score}", True, BLUE)
    time_text = font.render(f"Tiempo: {time_left}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 40))
    
    # Refrescar pantalla
    pygame.display.flip()
    clock.tick(30)
    
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Mensaje final
screen.fill(WHITE)
end_text = font.render(f"Juego Terminado! Puntos: {score}", True, BLUE)
screen.blit(end_text, (WIDTH//3, HEIGHT//2))
pygame.display.flip()
pygame.time.delay(3000)
pygame.quit()