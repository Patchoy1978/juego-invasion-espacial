import pygame
import random
import math
from pygame import mixer

pygame.init() #para inicalizarlo

pantalla = pygame.display.set_mode((800, 600)) # para crear la pantalla, en los parametros pasamos una tupla con los valores de la pantalla

# configuracion titulo e icono
pygame.display.set_caption('Invasión Espacial') # el titulo
icono = pygame.image.load('img\\ovni1.png') # para el icono, lo almacenamos en una variable
pygame.display.set_icon(icono) # para mostrar el icono
fondo = pygame.image.load('img\\fondoespacial.png')

# agregar musica
mixer.music.load('sonidos\\space-120280.mp3') # cargamos el archivo de sonido del juego
mixer.music.set_volume(0.3) # manipulamos el volumen
mixer.music.play(-1) # lo ponemos a sonar

# creamos las variables del jugador
img_jugador = pygame.image.load('img\\nave-espacial.png') # para el jugador, lo almacenamos en una variable
jugador_x = 368 # posicionamos el jugador en el eje x
jugador_y = 520 # posicionamos el jugador en el eje y
jugador_x_cambio = 0 # para cambiar el movimiento

# creamos las variables del enemigo
img_enemigo = [] # creamos una lista vacia
enemigo_x = [] # creamos una lista vacia
enemigo_y = [] # creamos una lista vacia
enemigo_x_cambio = [] # creamos una lista vacia
enemigo_y_cambio = [] # creamos una lista vacia
cantidad_enemigos = 10 # crea 10 enemigos

for e in range(cantidad_enemigos): # con el bucle creamos los enemigos

    # llenamos las listas
    img_enemigo.append(pygame.image.load('img\\astronaveenemigo64.png')) # para el jugador, lo almacenamos en una variable
    enemigo_x.append(random.randint(0,736)) # posicionamos el enemigo en el eje x
    enemigo_y.append(random.randint(2, 200)) # posicionamos el enemigo en el eje y
    enemigo_x_cambio.append(1) # para cambiar el movimiento en horizontal
    enemigo_y_cambio.append(85) # para cambiar el movimiento en vertical

# creamos las variables de la bala
balas = []
img_bala = pygame.image.load('img\\bala124.png') # para el jugador, lo almacenamos en una variable
bala_x = 0 # posicionamos la bala segun el jugador en el eje x
bala_y = 480 # posicionamos de donde sale la bala en el eje y
bala_x_cambio = 0 # para cambiar el movimiento en horizontal
bala_y_cambio = 3 # para cambiar el movimiento en vertical
bala_visible = False # inicia en false porque aun no se ha disparado

# creamos las variables de la explosion
img_explosion = pygame.image.load('img\\explosion64.png') # cargamos la imagen de la explosion
explosion_position = None # damos la posicion de la explosion
explosion_duration = 0 # la duracion de la explosion

# puntaje
puntaje = 0 # inicamos la variable que contiene el puntaje en 0 para irla incrementando
fuente = pygame.font.Font('fonts\\Fastest.ttf',16) # creamos la fuente para mostrar resultados
texto_x = 10 # posicion del texto
texto_y = 10 # posicion del texto
blanco = (255,255,255) # color del texto

# texto final del juego
fuente_final = pygame.font.Font('fonts\\Fastest.ttf', 40) # fuente del texto


# creamos el metodo para el mensaje final
def texto_final():

    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, blanco) # creamos una variable y renderizamos el texto

    pantalla.blit(mi_fuente_final, (60, 200)) # mostramos en la pantalla el texto

# funcion mostrar puntaje
def mostrar_puntaje(x, y):

    texto = fuente.render(f'Puntaje: {puntaje}', True, blanco) # generemos el texto
    pantalla.blit(texto, (x, y)) # para mostrarlo

# funcion del jugador
def jugador(x, y):

    pantalla.blit(img_jugador, (x, y)) # ponemos la imagen del jugador

# funcion del enemigo
def enemigo(x, y, ene):

    pantalla.blit(img_enemigo[ene], (x, y)) # ponemos los enemigos

# funcion disparar bala
def disparar_bala(x, y):

    global bala_visible # llamamos a la variable de una forma global

    bala_visible = True # la vomlvemos a true para que salga la bala

    pantalla.blit(img_bala, (x + 16, y + 16)) # para que la bala aparezca

# funcion detectar coliciones
def hay_colision(x_1, y_1, x_2, y_2 ):

    distancia = math.sqrt((math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))) # para almacenar el numero de pixeles que hay entre los objetos

    if distancia < 27:

        return True

    else:

        return False

# creamos el loop
se_ejecuta = True # creamos una variable
while se_ejecuta:

    #imagen de fondo
    pantalla.blit(fondo, (0, 0)) # ponemos la imagen de la pantalla

    # renderizar enemigos
    for e in range(cantidad_enemigos): # recorremos el bucle para traer a los enemigos

        enemigo(enemigo_x[e], enemigo_y[e], e) # llamamos a la funcion

    #jugador_x += 0.1 # para moverse en el eje x, ejemplo para ver como se mueve

    # iterar eventos
    for evento in pygame.event.get(): # evento revisa en todos los eventos que contien pygame

        if evento.type == pygame.QUIT: # si el evento es igual a pygame.QUIT cierra el programa

            se_ejecuta = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN: # para que cuando se precione una tecla

            if evento.key == pygame.K_LEFT: # para que la tecla flecha izq funcione

                jugador_x_cambio = -1 # la velocidad del movimiento

            if evento.key == pygame.K_RIGHT: # para que la tecla flecha der funcione

                jugador_x_cambio = +1 # la velocidad del movimiento

            if evento.key == pygame.K_SPACE: # usamos la barra espaciadora

                sonido_bala = mixer.Sound('sonidos\\disparo-6055.mp3') # cargamos el sonido de la bala

                mixer.Sound.play(sonido_bala) # lo ponemos a sonar

                nueva_bala = {'x' : jugador_x, 'y' : jugador_y, 'velocidad' : -5} # almacenamos en una variable un diccionario

                balas.append(nueva_bala) # agregamos esta nueva bala a la lista

        # evento soltar teclas
        if evento.type == pygame.KEYUP: # para que cuando se suelte una tecla

            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT: # comprobacion

                jugador_x_cambio = 0 # para que se detenga el movimiento

    # modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio # para actualizar el movimiento

    # mantener el jugador en la ventana
    if jugador_x <= 2:

        jugador_x = 2

    elif jugador_x >= 734:

        jugador_x = 734

    # modificar la ubicacion del enemigo

    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 488:

            for i in range(cantidad_enemigos): # recorremos la lista  de enemigos

                enemigo_y[i] = 700 # mandamos a los enemigos a esta posicion

            texto_final() # llamamos a la funcion para el fin del juego

            break

        enemigo_x[e] += enemigo_x_cambio[e]  # para actualizar el movimiento

        # mantener el enemigo en la ventana
        if enemigo_x[e] <= 2:

            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]

        elif enemigo_x[e] >= 734:

            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        for bala in balas:

            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala['x'], bala['y'])  # almacenamos el valor

            if colision_bala_enemigo:  # creamos la comprobacion

                sonido_colision = mixer.Sound('sonidos\\explosion-91872.mp3') # cargamos el sonido
                sonido_colision.play() # lo ponemos a sonar
                explosion_position = (enemigo_x[e], enemigo_y[e]) # para cuando impacta al enemigo
                explosion_duration = 15 # duarcion de la imagen de la explosion
                balas.remove(bala)
                puntaje += 100 # puntaje que le damos al jugador al matar los enemigos
                enemigo_x[e] = random.randint(0, 736)  # posicionamos el enemigo en el eje x
                enemigo_y[e] = random.randint(5, 200)  # posicionamos el enemigo en el eje y
                break

            enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento de la bala

    for bala in balas:

        bala['y'] += bala['velocidad']

        pantalla.blit(img_bala,(bala['x'] + 19, bala['y']))

        if bala['y'] < 0:

            balas.remove(bala)

    if explosion_duration > 0: # verificamos la duracion de la explosion
        pantalla.blit(img_explosion, explosion_position) # mostramos en la pantalla la imagen de la explosion
        explosion_duration -= 1 # la decrementamos para poder mostrarla cada vez

    jugador(jugador_x, jugador_y) # se llama a la funcion del juador

    mostrar_puntaje(texto_x, texto_y)

    pygame.display.update() # para actualizar
