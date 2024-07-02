import pygame
import json
from colores import *

def actualizar_pregunta(ventana,n_pregunta, preguntas: list, respuesta_a: list, respuesta_b: list, respuesta_c: list, fuente: str,):
    '''
    La  funcion va a recorrer un lista de datos y los renderiza por orden en pantalla hasta llegar al final de la lista

    Parametros:
    (ventana)  -> any
    (n_pregunta) -> int
    (preguntas) -> list
    (respuesta_a) -> list
    (respuesta_b) -> list
    (respuesta_c) -> list
    (fuente) -> str
    '''
    if n_pregunta <= len(preguntas) - 1:
        renderizar_texto(ventana, preguntas[n_pregunta], color_blanco, 150, fuente,)
        renderizar_texto(ventana, respuesta_a[n_pregunta], color_blanco, 260,fuente,)
        renderizar_texto(ventana, respuesta_b[n_pregunta], color_blanco, 330,fuente,)
        renderizar_texto(ventana, respuesta_c[n_pregunta], color_blanco,400, fuente,)


def renderizar_texto(pantalla, texto: str, color: str, posicion: int, fuente: str):
    """
    Esta funcion renderiza y blitea un texto.
    Parametros:
    (pantalla) -> any
    (texto)-> str
    (color) -> str
    (posicion_y) -> int
    (fuente) -> str
    """
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (640 - texto_renderizado.get_width()/2, posicion))

def obtener_nombre_jugador(ventana: any) -> str:
    '''
    La funcion pide el ingreso de un nombre al usuario y lo muestra por pantalla

    Parametros:
    (ventana): any
    
    Returns:
    (nombre): str   
    '''
    nombre = ""
    font_nombre = pygame.font.SysFont("Monocraft", 60)
    while True:
        
        imagen_fondo = pygame.image.load("Juego_Preguntados/fondo_menu.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (1280, 720))
        text_ingrese_nombre = font_nombre.render("Ingrese su nombre:", True, color_blanco)
        nombre_jugador = font_nombre.render(nombre, True, color_blanco)
        ventana.blit(imagen_fondo, (0, 0))
        ventana.blit(text_ingrese_nombre, (640 - text_ingrese_nombre.get_width() / 2, 250))
        ventana.blit(nombre_jugador,(640 - nombre_jugador.get_width() / 2, 400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return nombre
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode


def guardar_puntajes(nombre: str, puntaje: int):
    """
    Esta función crea (si no existe) un archivo json (scores.json) donde guarda los puntajes y el nombre de los jugadores,
    ordena los puntajes de forma descendente.

    Parámetros:
    (nombre) -> str
    (puntaje) -> int
    """
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    jugador_existente = False
    for jugador in scores:
        if jugador["nombre"] == nombre:
            jugador_existente = True
            if puntaje > jugador["score"]:
                jugador["score"] = puntaje
            break
    if not jugador_existente:
        scores.append({"nombre": nombre, "score": puntaje})
    scores = sorted(scores, key=lambda puntos: puntos["score"], reverse=True)[:3]
    with open('scores.json', 'w') as file:
        json.dump(scores, file)

def mostrar_puntajes(ventana):
    """
    La funcion va a carga un archivo json y carga los puntajes de forma ordenada para renderizarlos por pantalla.
    Parametros:
    (pantalla) -> any
    """
    fuente_titulo = pygame.font.SysFont("Monocraft", 80)
    fuente_puntaje = pygame.font.SysFont("Monocraft", 50)
    fuente_volver = pygame.font.SysFont("Monocraft", 40)
    boton_volver = pygame.Rect(540, 580, 200, 50)
    text_volver = fuente_volver.render("Volver", True, color_blanco)
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    imagen_fondo = pygame.image.load("Juego_Preguntados/fondo_menu.jpg")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (1280, 720))
    texto_titulo = fuente_titulo.render(str("Top 3 puntajes"),True,color_blanco)
    ventana.blit(imagen_fondo, (0,0))
    ventana.blit(texto_titulo,(640 - texto_titulo.get_width()/2,50))
    pygame.draw.rect(ventana, color_azul_claro, boton_volver, border_radius=15)
    ventana.blit(text_volver, (570, 585))
    y = 200
    for score in scores:
        texto_puntaje = fuente_puntaje.render(str(f"{ score['nombre']}: {score['score']}"),True,color_blanco)
        ventana.blit(texto_puntaje,(550,y))
        y += 50
    pygame.display.flip()
