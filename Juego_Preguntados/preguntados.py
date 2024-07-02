import pygame
from datos import lista
from colores import *
from biblioteca import *

pygame.init()
ventana = pygame.display.set_mode([1280, 720])
# LISTA PREGUNTAS
preguntas = []
respuestas_a = []
respuestas_b = []
respuestas_c = []
respuestas_correctas = []

for diccionario in lista:
    preguntas.append(diccionario["pregunta"])
    respuestas_a.append(diccionario["a"])
    respuestas_b.append(diccionario["b"])
    respuestas_c.append(diccionario["c"])
    respuestas_correctas.append(diccionario["correcta"])

# Imagenes
imagen_fondo = pygame.image.load("Juego_Preguntados/fondo_menu.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (1280, 720))
imagen_game = pygame.image.load("Juego_Preguntados/fondo_game.jpg")
imagen_game = pygame.transform.scale(imagen_game, (1280, 720))
logo = pygame.image.load("Juego_Preguntados\logo.png")
logo = pygame.transform.scale(logo, (180, 160))
corazon = pygame.image.load("Juego_Preguntados\corazon.png")
corazon = pygame.transform.scale(corazon, (40, 40))

# BOTONES
boton_jugar = pygame.Rect(495, 150, 290, 70)
boton_puntaje = pygame.Rect(495, 260, 290, 70)
boton_salir = pygame.Rect(495, 370, 290, 70)
boton_reiniciar = pygame.Rect(20, 30, 320, 70)
boton_pregunta = pygame.Rect(900, 30, 320, 70)
boton_volver = pygame.Rect(540, 580, 200, 50)
# preguntas
boton_a = pygame.Rect(475, 250, 340, 50)
boton_b = pygame.Rect(475, 320, 340, 50)
boton_c = pygame.Rect(475, 390, 340, 50)

# CONTADORES
puntaje = 0
n_pregunta = 0
pregunta = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""

# TEXTOS
font = pygame.font.SysFont("Monocraft", 50)
font_preguntas = pygame.font.SysFont("Monocraft", 30)
font_game_over = pygame.font.SysFont("Monocraft", 100)
font_puntaje = pygame.font.SysFont("Monocraft", 40)
text_start = font.render("Start", True, color_blanco)
text_puntaje = font.render("Puntaje", True, color_blanco)
text_salir = font.render("Salir", True, color_blanco)
text_reiniciar = font.render("Reiniciar", True, color_blanco)
text_preguntar = font.render("Pregunta", True, color_blanco)
text_score = font.render(f"Score: {puntaje}", True, color_blanco)
text_vidas = font.render("Vidas:", True, color_blanco)
text_volver = font_puntaje.render("Volver", True, color_blanco)

#SONIDOS
sonido_start = pygame.mixer.Sound("Juego_Preguntados\game-start-6104.mp3")
sonido_correcta = pygame.mixer.Sound("Juego_Preguntados\song_correcta2.mp3")
sonido_incorrecta = pygame.mixer.Sound("Juego_Preguntados\windows-error-sound.mp3")
sonido_start.set_volume(0.2)
sonido_correcta.set_volume(0.2)

# BANDERAS
game_over = False
menu = True
running = True
pregunto = False
errores = 0
esta_jugando = False
ver_puntajes = False
pedir_nombre = False
musica_menu = True
#============================================================================================
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # MENU
            if menu:
                if boton_jugar.collidepoint(event.pos):
                    musica_menu = False
                    sonido_start.play()
                    nombre = obtener_nombre_jugador(ventana)
                    game_over = False
                    menu = False
                    esta_jugando = True
                if boton_puntaje.collidepoint(event.pos):
                    sonido_start.play()
                    musica_menu = False
                    menu = False
                    ver_puntajes = True
                if boton_salir.collidepoint(event.pos):
                    running = False
            # JUEGO
            if not game_over and esta_jugando:
                if boton_pregunta.collidepoint(event.pos):
                    pregunto = True
                    errores = 0
                    actualizar_pregunta(ventana, n_pregunta, preguntas, respuestas_a, respuestas_b, respuestas_c,font_preguntas)

                if boton_reiniciar.collidepoint(event.pos):
                    puntaje = 0
                    n_pregunta = 0
                    errores = 0
                    pregunto = True
                    text_score = font.render(f"Score: {puntaje}", True, color_blanco)
                    actualizar_pregunta(ventana, n_pregunta, preguntas, respuestas_a, respuestas_b, respuestas_c,font_preguntas)

                if pregunto:
                    if boton_a.collidepoint(event.pos):
                        if respuestas_correctas[n_pregunta] == "a":
                            sonido_correcta.play()
                            puntaje += 10
                        else:
                            sonido_incorrecta.play()
                            errores += 1

                    elif boton_b.collidepoint(event.pos):
                        if respuestas_correctas[n_pregunta] == "b":
                            sonido_correcta.play()
                            puntaje += 10
                        else:
                            sonido_incorrecta.play()
                            errores += 1

                    elif boton_c.collidepoint(event.pos):
                        if respuestas_correctas[n_pregunta] == "c":
                            sonido_correcta.play()
                            puntaje += 10
                        else:
                            sonido_incorrecta.play()
                            errores += 1

                    if errores == 2 or respuestas_correctas[n_pregunta] == "a" and boton_a.collidepoint(event.pos) or respuestas_correctas[n_pregunta] == "b" and boton_b.collidepoint(event.pos) or respuestas_correctas[n_pregunta] == "c" and boton_c.collidepoint(event.pos):
                        n_pregunta += 1
                        text_score = font.render(f"Score: {puntaje}", True, color_blanco)
                        if n_pregunta >= len(preguntas) or errores == 2:
                            game_over = True
                        else:
                            actualizar_pregunta(ventana, n_pregunta, pregunta, respuesta_a, respuesta_b, respuesta_c,font_preguntas)
                            pregunto = False

            if ver_puntajes:
                if boton_volver.collidepoint(event.pos):
                    ver_puntajes = False
                    menu = True
                    musica_menu = True

            if game_over:
                if boton_volver.collidepoint(event.pos):
                    musica_menu = True
                    menu = True
                    esta_jugando = False
                    game_over = False
                    pedir_nombre = False
                    

    if menu:
        ventana.blit(imagen_fondo, (0, 0))
        ventana.blit(logo, (550, 0))
        pygame.draw.rect(ventana, color_azul, boton_jugar, border_radius=15)
        pygame.draw.rect(ventana, color_gris, boton_puntaje, border_radius=15)
        pygame.draw.rect(ventana, color_rojo, boton_salir, border_radius=15)
        ventana.blit(text_start, (570, 155))
        ventana.blit(text_puntaje, (535, 265))
        ventana.blit(text_salir, (570, 375))

    if esta_jugando:
        ventana.blit(imagen_game, (0, 0))
        ventana.blit(logo, (550, 0))
        pygame.draw.rect(ventana, color_azul_claro, boton_reiniciar, border_radius=15)
        pygame.draw.rect(ventana, color_azul_claro, boton_pregunta, border_radius=15)
        ventana.blit(text_reiniciar, (25, 30))
        ventana.blit(text_preguntar, (910, 30))
        ventana.blit(text_score, (550, 640))
        ventana.blit(text_vidas, (550, 570))
        if pregunto:
            pygame.draw.rect(ventana, color_azul_claro, boton_a, border_radius=15)
            pygame.draw.rect(ventana, color_azul_claro, boton_b, border_radius=15)
            pygame.draw.rect(ventana, color_azul_claro, boton_c, border_radius=15)
            actualizar_pregunta(ventana, n_pregunta, preguntas, respuestas_a, respuestas_b, respuestas_c,font_preguntas)
        if errores == 0:
            ventana.blit(corazon, (740, 580))
            ventana.blit(corazon, (790, 580))
        elif errores == 1:
            ventana.blit(corazon, (740, 580))

    if game_over:
        guardar_puntajes(nombre,puntaje)
        nombre_jugador = font_puntaje.render(nombre, True, color_blanco)
        ventana.blit(imagen_fondo, (0, 0))
        text_game_over = font_game_over.render("GAME OVER", True, color_blanco)
        ventana.blit(text_game_over, (640 - text_game_over.get_width() / 2, 100))
        ventana.blit(nombre_jugador,(640 - nombre_jugador.get_width() / 2, 300))
        ventana.blit(text_score, (640 - text_score.get_width() / 2, 400))
        pygame.draw.rect(ventana, color_azul_claro, boton_volver, border_radius=15)
        ventana.blit(text_volver, (570, 585))

    if ver_puntajes:
        mostrar_puntajes(ventana)

    pygame.display.flip()
pygame.quit()