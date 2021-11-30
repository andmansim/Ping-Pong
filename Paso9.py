#Parte9:
#Puntuación de los jugadores:

# Puntuación de la pelota
self.puntuacion = 0
self.puntuacion_ia = 0

#Modificar la puntuación
def rebotar(self):
    if self.x <= -self.ancho:
        self.reiniciar()
        self.puntuacion_ia += 1
    if self.x >= VENTANA_HORI:
        self.reiniciar()
        self.puntuacion += 1
        
#Ventana la puntuación de ambos jugadores:
#Color del texto
NEGRO = (0, 0, 0)  # Color del texto (RGB)
