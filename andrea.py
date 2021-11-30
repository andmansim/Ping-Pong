#Parte 1:
#Importación de módulos
import pygame
from pygame.locals import *

#Definición de constantes

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)

#Inicialización
pygame.init()
# Inicialización de la superficie de dibujo (display surface)
ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
pygame.display.set_caption("Pong 1")