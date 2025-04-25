import pygame
import sys
import os

# Inicializar el mezclador de sonido
pygame.mixer.init()



if os.system("clear") != 0: os.system("cls")

# Preguntar el peso al usuario
try:
    peso = float(input("¿Cuánto pesas? (en kg): "))

except ValueError:
    print("Por favor, introduce un número válido.")
    sys.exit()
 
    

# Inicializar pygame
pygame.init()



# Configurar pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Peso")

# Color de fondo
BG_COLOR = (255, 255, 255)

# Cargar imagen
imagen = pygame.image.load("./img/fatNot.jpg")  # Asegúrate de que esté en la misma carpeta
imagen = pygame.transform.scale(imagen, (200, 200))  # Redimensionar si es necesario

##Coordenadad de la imagen 

img_x = WIDTH // 2 - 40
img_y = HEIGHT // 2 - 100
img_rect = imagen.get_rect(center=(img_x, img_y))

angle = 0 # Angulo de la imagen

# Control de FPS
clock = pygame.time.Clock()

# Variable para controlar la reproducción de la música
musica_activada = False

# Bucle del juego
running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if peso <= 100:
       print("Peso normal")
       break
  
    # Mostrar imagen si el peso es mayor a 100
    elif peso > 100:
        rotated_img = pygame.transform.rotate(imagen, angle)
        rotated_rext = rotated_img.get_rect(center=img_rect.center)
        screen.blit(rotated_img, rotated_rext)
        angle += 2 ##Velocidad
        
    if not musica_activada:
        pygame.mixer.music.load("./music/alarm.mp3")  
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Repetir en bucle
        musica_activada = True

    pygame.display.flip()
    clock.tick(60)

# Cerrar pygame
pygame.quit()
sys.exit()
