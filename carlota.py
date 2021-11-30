import random
import pygame
from pygame.locals import QUIT

VENTANA_HORI = 800
VENTANA_VERT = 600
FPS = 60
BLANCO = (255, 255, 255)

class PelotaPong:
    def __init__(self, fichero_imagen):
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        self.ancho, self.alto = self.imagen.get_size()

        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])


def main():
    pygame.init()

    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 3")

    pelota = PelotaPong("bola_roja.png")

    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()