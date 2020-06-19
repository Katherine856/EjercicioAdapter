import pygame
from P2.Derecha import *
from P2.Izquierda import *
from P2.Quieto import *
from pygame.locals import *

der = Derecha()
izq = Izquierda()
qui = Quieto()

derecha = der.getDerecha()
izquierda = izq.getIzquierda()
quieto = qui.getQuieto()

matriz = []

#Inicializar la matriz de inecuaciones
for i in range(3):
    matriz.append([])
    for j in range(10):
        matriz[i].append(None)

for j in range(10):
    matriz[0][j] = quieto[j]

for j in range(10):
    matriz[1][j] = derecha[j]

for j in range(10):
    matriz[2][j] = izquierda[j]

frame = 0
indice = 0

pygame.init()
 
pantalla = pygame.display.set_mode((720,320),0,32)
x = 360
y = 100

def cargar(indice):
    global frame, x, y
    frame = (frame+1) % 10;
    pantalla.blit(matriz[indice][frame], (x, y));
     
reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed()
 
    if(pygame.key.get_pressed()):
        if pulsada[K_a]:
            x -= 5
            indice = 2
        elif pulsada[K_d]:
            indice = 1
            x += 5
        else:
            indice = 0
        
    reloj.tick(25)
    pantalla.fill((255,255,255))
    cargar(indice)
    pygame.display.update()
