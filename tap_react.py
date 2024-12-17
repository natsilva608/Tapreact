import pygame
import random
import csv
import time
import sys
import os

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tap_react")

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Cargar tipografía
font_path = "imagenes/tipografia.ttf"
fontyy = pygame.font.Font(font_path,22)
font_size = 24
font = pygame.font.Font(font_path, font_size)
font_size2 = 15
font2 = pygame.font.Font(font_path, font_size2)
font_size3 = 25
font3 = pygame.font.Font(font_path, font_size3)
fontflecha = "imagenes/arial.ttf"
fontflechasize = 40
fontflechas = pygame.font.Font(fontflecha,fontflechasize)
font1game = 20
fontgame1= pygame.font.Font(font_path,font1game)


# Cargar sonidos
pygame.mixer.init()  # Inicializar el mezclador de audio
arriba = pygame.mixer.Sound("imagenes/sonidoarriba.mp3")
abajo = pygame.mixer.Sound("imagenes/sonidoabajo.mp3")
izq = pygame.mixer.Sound("imagenes/sonidoizq.mp3")
der = pygame.mixer.Sound("imagenes/sonidoder.mp3")

# Cargar imágenes

estrella11 = pygame.image.load("imagenes/tresestrellas1.png")
estrella1verde = pygame.transform.scale(estrella11,(180,100))
estrella22 = pygame.image.load("imagenes/tresestrellas2.png")
estrella2verde = pygame.transform.scale(estrella22,(180,100))
estrella33 = pygame.image.load("imagenes/tresestrellas3.png")
estrella3verde = pygame.transform.scale(estrella33,(180,100))

estrella111 = pygame.image.load("imagenes/treestrellas1.png")
estrella1azul = pygame.transform.scale(estrella11,(180,100))
estrella222 = pygame.image.load("imagenes/treestrellas2.png")
estrella2azul = pygame.transform.scale(estrella22,(180,100))
estrella333 = pygame.image.load("imagenes/treestrellas3.png")
estrella3azul = pygame.transform.scale(estrella33,(180,100))

estrella1111 = pygame.image.load("imagenes/trestrellas1.png")
estrella1rosa = pygame.transform.scale(estrella11,(180,100))
estrella2222= pygame.image.load("imagenes/trestrellas2.png")
estrella2rosa = pygame.transform.scale(estrella22,(180,100))
estrella3333 = pygame.image.load("imagenes/trestrellas3.png")
estrella3rosa = pygame.transform.scale(estrella33,(180,100))



meteor = pygame.image.load("imagenes/meteoro.png")
meteoro = pygame.transform.scale(meteor, (1,1))
background_image = pygame.image.load("imagenes/pantalla.png")
button_image = pygame.image.load("imagenes/botonmenu.png")  # boton del menu
button_imagen1menu = pygame.transform.scale(button_image, (180, 50))  # boton del menu escala
button_imagen11 = pygame.image.load("imagenes/boton1.png")
button_imagen1 = pygame.transform.scale(button_imagen11, (220, 65))
button_imagenins = pygame.transform.scale(button_imagen11, (290, 65))
boton_game1 =pygame.image.load("imagenes/botongame1.png")
boton_game2 =pygame.image.load("imagenes/botongame2.png")
boton_game3 =pygame.image.load("imagenes/botongame3.png")
botonrepuesto = pygame.transform.scale(button_imagen11, (230,45))  # boton del menu escala
gamefrogsbg1 = pygame.image.load("imagenes/gamefrogsbg1.png")
gamefrogsbg2 = pygame.image.load("imagenes/gamefrogsbg2.png")
rabittsbackgroundgame = pygame.image.load("imagenes/rabittsbackgroundgame.png")

botonrosa = pygame.image.load("imagenes/botonrosa.png")
botonrosaa = pygame.transform.scale(botonrosa,(120,45))
botonrosains = pygame.transform.scale(botonrosa,(290,65))
botonazul = pygame.image.load("imagenes/botonazul.png")
botonazull = pygame.transform.scale(botonazul,(120,45))
botonazulins = pygame.transform.scale(botonazul,(290,65))
button_games=pygame.transform.scale(button_imagen11,(350,100)) #boton game1game2game3
botonbackk = pygame.image.load("imagenes/botonback.png")
botonback = pygame.transform.scale(button_imagen11,(120,45))
botonca = pygame.transform.scale(botonbackk,(120,45))
botoncaa = pygame.transform.scale(botonbackk,(120,45))

sound_path = "imagenes/sonido.mp3"
sound = pygame.mixer.Sound(sound_path)

# Crear el texto
text_surface = fontyy.render("Press space to start...", True, (BLACK))
text_surface2 = fontyy.render("Press space to start...", True, (WHITE))

# Posición del texto
text_x1 = screen_width // 2 - text_surface.get_width() // 2
text_y1 = 90 + 245-5

text_x2 = screen_width // 2+3 - text_surface2.get_width() // 2-9
text_y2 = 90 + 245-5

# Cargar los frames de la animación insmonkeys
animation_framesmmt = []
for i in range(1, 19):  
    framemmt = pygame.image.load(os.path.join("instructionsfrogs", f"insfrogs{i}.png"))
    animation_framesmmt.append(framemmt)
# Inicializar variables para la animación
current_frammmt = 0
frame_delaymmt =80  # Controlar la velocidad de la animación (mayor número = más lento)
frame_counter = 0

# Cargar los frames de la animación insmonkeys
animation_framesmm = []
for i in range(1, 13):  
    framemm = pygame.image.load(os.path.join("instructionsmonkeys", f"insmonkeys{i}.png"))
    animation_framesmm.append(framemm)
# Inicializar variables para la animación
current_frammm = 0
frame_delaymm =80  # Controlar la velocidad de la animación (mayor número = más lento)
frame_counter = 0

# Cargar los frames de la animación insrabbits
animation_frameszz = []
for i in range(1, 20):  
    framezz = pygame.image.load(os.path.join("instructionsrabbits", f"insrabbits{i}.png"))
    animation_frameszz.append(framezz)
# Inicializar variables para la animación
current_framzz = 0
frame_delayzz =70 # Controlar la velocidad de la animación (mayor número = más lento)
frame_counter = 0

# Cargar los frames de la animación rabbits
animation_framesz = []
for i in range(1, 21):  
    framez = pygame.image.load(os.path.join("worldrabbits", f"rabbits{i}.png"))
    animation_framesz.append(framez)

# Inicializar variables para la animación
current_framz = 0
frame_delayz =80  # Controlar la velocidad de la animación (mayor número = más lento)
frame_counter = 0

# Cargar los frames de la animación monkeys
animation_framesm = []
for i in range(1, 5):  
    framem = pygame.image.load(os.path.join("worldmonkeys", f"monkey{i}.png"))
    animation_framesm.append(framem)

# Inicializar variables para la animación
current_framm = 0
frame_delaym =80  # Controlar la velocidad de la animación (mayor número = más lento)
frame_counter = 0

# Cargar los frames de la animación frogs
animation_framesa = []
for i in range(1, 17):  # Asumiendo que los frames van de 1 a 16
    framea = pygame.image.load(os.path.join("worldfrogs", f"world{i}.png"))
    animation_framesa.append(framea)

# Inicializar variables para la animación
current_frame = 0
frame_delaya =80  # Controlar la velocidad de la animación (mayor número = más lento)
frame_counter = 0

# Función para la ventana de "registrer"
# Cargar imágenes de la animación "playregistrer"
playregistrer_frames = [
    pygame.image.load('playregistrer/pr1.png'),
    pygame.image.load('playregistrer/pr2.png')
]

# Configurar velocidad de animación
frame_index = 0
animation_timer = pygame.time.get_ticks()
fps = 2  # Velocidad de la animación en cuadros por segundo
frame_duration = 1000 // fps  # Duración de cada cuadro en milisegundos

# Animación de fondo
bgg_frames = [pygame.image.load("playregistrer/pr1.png"), pygame.image.load("playregistrer/pr2.png")]
bgg_index = 0
bgg_frame_duration = 500  # Duración de cada frame en milisegundos (2 FPS)


def save_game_result(nickname, game, result):
    """
    Guarda el resultado de un juego en la base de datos del usuario.
    Si el usuario ya tiene resultados previos, se agregará al historial.

    :param nickname: El nombre del usuario.
    :param game: El nombre del juego (e.g., "Game 1").
    :param result: El resultado obtenido en el juego.
    """
    database_file = "corrected_database.csv"
    temp_file = "temp_corrected_database.csv"
    updated = False

    try:
        with open(database_file, mode="r") as file, open(temp_file, mode="w", newline="") as temp:
            reader = csv.reader(file)
            writer = csv.writer(temp)

            for row in reader:
                if row[0] == nickname:
                    # Si el usuario ya existe, agrega el resultado al historial
                    if len(row) < 3:
                        row.append(f"{game}: {result}")
                    else:
                        row[2] += f" | {game}: {result}"
                    updated = True
                writer.writerow(row)

        # Si el usuario no estaba en la base de datos, agrégalo
        if not updated:
            with open(temp_file, mode="a", newline="") as temp:
                writer = csv.writer(temp)
                writer.writerow([nickname, "", f"{game}: {result}"])


    except FileNotFoundError:
        # Si no existe la base de datos, créala y agrega el resultado
        with open(database_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nickname, "", f"{game}: {result}"])

# Función para detectar si el mouse está sobre un botón
def is_mouse_over_button(mouse_pos, x, y, width, height):
    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height

# Simular las funciones de guardar y botones
def save_to_database(nickname, password):
    pass  # Aquí puedes agregar la lógica para guardar en una base de datos

# Función para verificar si el mouse está sobre un botón
def is_mouse_over_button(mouse_pos, button_x, button_y, button_width, button_height):
    return button_x <= mouse_pos[0] <= button_x + button_width and \
           button_y <= mouse_pos[1] <= button_y + button_height
# Función para guardar datos en un archivo CSV
def save_to_database(nickname, password):
    with open("corrected_database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nickname, password])

# Función para validar los datos ingresados
def validate_credentials(nickname, password):
    try:
        with open("corrected_database.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row == [nickname, password]:
                    return True
    except FileNotFoundError:
        print("Base de datos no encontrada. Registre un usuario primero.")
    return False

#ventana de game1instructions
def game1instructions():
    global current_frammmt, frame_counter
    running=True
    while running:
        screen.blit(animation_framesmmt[current_frammmt], (0, 0))

        # Actualizar el frame de la animación
        frame_counter += 1
        if frame_counter >= frame_delaymmt:
            frame_counter = 0
            current_frammmt = (current_frammmt + 1) % len(animation_framesmmt)

        text_instructionstitle = font3.render("INSTRUCTIONS GAME 1",True,(WHITE))
        text_instructiontitle = font3.render("INSTRUCTIONS GAME 1",True,(BLACK))

        text_instructions1 = font2.render("1.-Aparecerá una cuenta regresiva en pantalla.",True,(BLACK))
        text_instructions12 = font2.render("¡Espera atento!",True,(BLACK))
        text_instructions11 = font2.render("2.-Falta una rana en el estanque.",True,(BLACK))
        text_instructions112 = font2.render("No presiones ninguna tecla en este momento.",True,(BLACK))
        text_instructions111 = font2.render("3.-Cuando aparezca la rana, presiona",True,(BLACK))
        text_instructions1112 = font2.render("la barra espaciadora lo más rápido posible.",True,(BLACK))
        text_instructions1111 = font2.render("4.-Se medirá tu tiempo de reacción desde el  ",True,(BLACK))
        text_instructions11112 = font2.render("momento en que el círculo cambia a rojo hasta ",True,(BLACK))
        text_instructions111122 = font2.render("que presionas la tecla.",True,(BLACK))
        text_instructions11111 = font2.render("5.-Al final, podrás ver tus resultados en",True,(BLACK))
        text_instructions111112 = font2.render("la pantalla.",True,(BLACK))

        screen.blit(text_instructionstitle,(150,55))
        screen.blit(text_instructiontitle,(145,55))

        screen.blit(text_instructions1,(70,105))
        screen.blit(text_instructions12,(80,135))

        screen.blit(text_instructions11,(70,185))
        screen.blit(text_instructions112,(80,215))

        screen.blit(text_instructions111,(70,265))
        screen.blit(text_instructions1112,(80,295))


        screen.blit(text_instructions1111,(70,345))
        screen.blit(text_instructions11112,(80,375))
        screen.blit(text_instructions111122,(80,405))

        screen.blit(text_instructions11111,(70,455))
        screen.blit(text_instructions111112,(80,485))


        # Botón "Back" para regresar a la ventana anterior
        back_button_x = screen_width // 2 - botonback.get_width() // 2 + 240
        back_button_y = screen_height - botonback.get_height() - 140
        screen.blit(botonback, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, botonback.get_width(),botonback.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonback.get_width() // 2 - back_text.get_width() // 2,
                                back_button_y + botonback.get_height() // 2 - back_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, button_image.get_width(), button_image.get_height()):
                    return  # Regresar a la ventana anterior

    pygame.quit()

def game1play():
    running = True
    screen.blit(gamefrogsbg1, (0, 0))

    # Mostrar cuenta regresiva
    for i in range(3, 0, -1):
        screen.blit(gamefrogsbg1, (0, 0))
        countdown_text = font.render(str(i), True, BLACK)
        screen.blit(
            countdown_text, 
            (screen_width // 2 - countdown_text.get_width() // 2 - 5, screen_height // 2 - countdown_text.get_height() // 2 - 40)
        )
        countdown_text = font.render(str(i), True, WHITE)
        screen.blit(
            countdown_text, 
            (screen_width // 2 - countdown_text.get_width() // 2, screen_height // 2 - countdown_text.get_height() // 2 - 40)
        )
        pygame.display.flip()
        pygame.time.delay(1000)

    screen.blit(gamefrogsbg1, (0, 0))  # Redibujar el fondo (limpia la pantalla)
    pygame.display.flip()

    # Crear círculo
    circle_color = BLACK
    circle_radius = 1
    circle_position = (screen_width // 2, screen_height // 2 - 50)
    pygame.draw.circle(screen, circle_color, circle_position, circle_radius)
    pygame.display.flip()

    # Esperar un tiempo aleatorio entre 2 y 6 segundos
    wait_time = random.uniform(2, 6)
    pygame.time.delay(int(wait_time * 1000))

    # Cambiar el color del círculo a rojo
    screen.blit(gamefrogsbg2, (0, 0))
    screen.blit(meteoro, (circle_position[0] - meteoro.get_width() // 2, circle_position[1] - meteoro.get_height() // 2))
    pygame.display.flip()

    # Tomar el tiempo de reacción
    reaction_start_time = time.time()
    reaction_time = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reaction_time = time.time() - reaction_start_time
                    running = False

    # Guardar el resultado en la base de datos
    nickname = "nickname"  # Reemplaza con la variable que almacena el nombre del usuario actual
    result = f"Tiempo de reacción: {reaction_time:.3f} segundos"
    save_game_result(nickname, "Game 1", result)

    # Determinar el nivel basado en el tiempo de reacción
    if reaction_time < 0.3:
        nivel = "nivel: avanzado"
    elif 0.3 <= reaction_time <= 0.7:
        nivel = "nivel: medio"
    else:
        nivel = "nivel: bajo"

    # Mostrar ventana de resultados indefinidamente
    result_displaying = True
    start_time = pygame.time.get_ticks()  # Tiempo inicial para controlar los intervalos
    current_image = estrella1verde

    while result_displaying:
        global current_frammmt, frame_counter
        screen.blit(animation_framesmmt[current_frammmt], (0, 0))
        frame_counter += 1
        if frame_counter >= frame_delaymmt:
            frame_counter = 0
            current_frammmt = (current_frammmt + 1) % len(animation_framesmmt)
        
        titleresult1 = fontgame1.render("RESULTS", True, WHITE)
        result_text = fontgame1.render(f"Tiempo de reacción: {reaction_time:.3f} segundos", True, WHITE)
        nivel_text = fontgame1.render(nivel, True, WHITE)

        screen.blit(
            result_text, 
            (screen_width // 2 - 40 - result_text.get_width() // 2 + 30, screen_height // 2 - result_text.get_height() // 2 - 140)
        )
        screen.blit(
            nivel_text,
            (screen_width // 2 - nivel_text.get_width() // 2 - 10, screen_height // 2 - nivel_text.get_height() // 2 - 60)
        )
        screen.blit(
            titleresult1,
            (screen_width // 2 + 40 - nivel_text.get_width() // 2, screen_height // 2 - nivel_text.get_height() // 2 - 260)
        )

        # Mostrar imagen según el nivel
        elapsed_time = pygame.time.get_ticks() - start_time
        if nivel == "nivel: medio" and elapsed_time > 1500:
            current_image = estrella2verde
        elif nivel == "nivel: avanzado":
            if elapsed_time > 3000:
                current_image = estrella3verde
            elif elapsed_time > 1500:
                current_image = estrella2verde

        screen.blit(current_image, (screen_width // 2 - current_image.get_width() // 2, screen_height // 2))

        # Botones "Again" y "Cancel"
        back_button_x = screen_width // 2 - botonca.get_width() // 2 + 240
        back_button_y = screen_height - botonca.get_height() - 180
        screen.blit(botonca, (back_button_x, back_button_y))

        if is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, botonca.get_width(), botonca.get_height()):
            back_text_color = WHITE
        else:
            back_text_color = (0, 0, 0)

        back_text = font.render("Again", True, back_text_color)
        screen.blit(
            back_text,
            (
                back_button_x + botoncaa.get_width() // 2 - back_text.get_width() // 2,
                back_button_y + botoncaa.get_height() // 2 - back_text.get_height() // 2,
            ),
        )

        cancel_button_x = screen_width // 2 - botonca.get_width() // 2 - 240
        cancel_button_y = screen_height - botonca.get_height() - 180
        screen.blit(botonca, (cancel_button_x, cancel_button_y))

        if is_mouse_over_button(pygame.mouse.get_pos(), cancel_button_x, cancel_button_y, botonca.get_width(), botonca.get_height()):
            cancel_text_color = WHITE
        else:
            cancel_text_color = (0, 0, 0)

        cancel_text = font.render("Cancel", True, cancel_text_color)
        screen.blit(
            cancel_text,
            (
                cancel_button_x + botonca.get_width() // 2 - cancel_text.get_width() // 2,
                cancel_button_y + botonca.get_height() // 2 - cancel_text.get_height() // 2,
            ),
        )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return reaction_time

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_over_button(
                    pygame.mouse.get_pos(),
                    back_button_x,
                    back_button_y,
                    botoncaa.get_width(),
                    botoncaa.get_height(),
                ):
                    return game1play()

                if is_mouse_over_button(
                    pygame.mouse.get_pos(),
                    cancel_button_x,
                    cancel_button_y,
                    botonca.get_width(),
                    botonca.get_height(),
                ):
                    return game1menu()

    pygame.quit()


#ventana de game1menu
def game1menu():
    global current_frame, frame_counter
    running = True
    while running:
        # Dibujar el frame actual de la animación como fondo
        screen.blit(animation_framesa[current_frame], (0, 0))

        # Actualizar el frame de la animación
        frame_counter += 1
        if frame_counter >= frame_delaya:
            frame_counter = 0
            current_frame = (current_frame + 1) % len(animation_framesa)

        # Botón "play"
        play_button_xx = screen_width // 2 - button_imagen1.get_width() // 2
        play_button_yy = screen_height // 2 - button_imagen1.get_height()-60
        screen.blit(button_imagen1, (play_button_xx, play_button_yy))
        play_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), play_button_xx, play_button_yy, button_imagen1.get_width(), button_imagen1.get_height()) else (0,0,0)
        play_text = font.render("play", True, play_text_color)
        screen.blit(play_text, (play_button_xx + button_imagen1.get_width() // 2 - play_text.get_width() // 2,
                                   play_button_yy + button_imagen1.get_height() // 2 - play_text.get_height() // 2))

        # Botón "instructions"
        play_button_x = screen_width // 2 - button_imagenins.get_width() // 2+5
        play_button_y = screen_height // 2 - button_imagenins.get_height()-50
        instructionsbutton_x = play_button_x
        instructions_button_y = play_button_y + button_imagenins.get_height() + 80
        screen.blit(button_imagenins, (instructionsbutton_x, instructions_button_y))
        instructions_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), instructionsbutton_x, instructions_button_y, button_imagenins.get_width(), button_imagenins.get_height()) else (0,0,0)
        instructions_text = font.render("instructions", True, instructions_text_color)
        screen.blit(instructions_text, (instructionsbutton_x + button_imagenins.get_width() // 2 - instructions_text.get_width() // 2,
                                       instructions_button_y + button_imagenins.get_height() // 2 - instructions_text.get_height() // 2))

        # Botón "Back" para regresar a la ventana anterior
        back_button_x = screen_width // 2 - botonback.get_width() // 2+240
        back_button_y = screen_height - botonback.get_height() -140
        screen.blit(botonback, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, botonback.get_width(), botonback.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonback.get_width() // 2 - back_text.get_width() // 2,
                               back_button_y + botonback.get_height() // 2 - back_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if is_mouse_over_button(pygame.mouse.get_pos(), play_button_x, play_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    game1play()
                elif is_mouse_over_button(pygame.mouse.get_pos(), instructionsbutton_x, instructions_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    game1instructions()
                elif is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    return  # Regresar a la ventana anterior

    pygame.quit()

#ventana de game2instructions
def game2instructions():
    global current_frammm, frame_counter
    running=True
    while running:
        screen.blit(animation_framesmm[current_frammm], (0, 0))

        # Actualizar el frame de la animación
        frame_counter += 1
        if frame_counter >= frame_delaymm:
            frame_counter = 0
            current_frammm = (current_frammm + 1) % len(animation_framesmm)

        text_instructionstitl = font3.render("INSTRUCTIONS GAME 2",True,(WHITE))
        text_instructiontit = font3.render("INSTRUCTIONS GAME 2",True,(BLACK))

        instructions1 = font2.render("1.-Tras la cuenta regresiva, se activará ",True,(BLACK))
        instructions12 = font2.render("una espera aleatoria.",True,(BLACK))
        instructions11 = font2.render("2.-Cuando escuches el sonido, presiona la barra ",True,(BLACK))
        instructions112 = font2.render("espaciadora lo más rápido posible.",True,(BLACK))
        instructions111 = font2.render("3.-Al final, podrás ver los resultados en",True,(BLACK))
        instructions1112 = font2.render("la pantalla.",True,(BLACK))


        screen.blit(text_instructionstitl,(150,55))
        screen.blit(text_instructiontit,(145,55))

        screen.blit(instructions1,(70,160))
        screen.blit(instructions12,(80,190))

        screen.blit(instructions11,(70,260))
        screen.blit(instructions112,(80,290))

        screen.blit(instructions111,(70,360))
        screen.blit(instructions1112,(80,390))

        # Botón "Back" para regresar a la ventana anterior
        back_button_x = screen_width // 2 - botonazull.get_width() // 2 + 240
        back_button_y = screen_height - botonazull.get_height() - 140
        screen.blit(botonazull, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, botonazull.get_width(), botonazull.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonazull.get_width() // 2 - back_text.get_width() // 2,
                                back_button_y + botonazull.get_height() // 2 - back_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, button_image.get_width(), button_image.get_height()):
                    return  # Regresar a la ventana anterior

    pygame.quit()

#ventana de game2play
def game2play():
    # Cargar los fotogramas del fondo animado
    bg_frame_1 = pygame.image.load("gamemonkeysbg/gamemonkeysbgt1.png").convert()
    bg_frame_2 = pygame.image.load("gamemonkeysbg/gamemonkeysbgt2.png").convert()

    # Función para mostrar texto en pantalla
    def draw_text(text, x, y, font, color):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    # Función para animar el fondo
    def animate_background():
        nonlocal bg_toggle, last_frame_time
        current_time = time.time()
        if current_time - last_frame_time >= 0.6:  # Cambiar frame cada 0.6 segundos
            bg_toggle = not bg_toggle
            last_frame_time = current_time
        screen.blit(bg_frame_1 if bg_toggle else bg_frame_2, (0, 0))

    # Pantalla de cuenta regresiva
    def countdown():
        for i in range(3, 0, -1):
            animate_background()
            draw_text(str(i), screen_width // 2, screen_height // 2 - 30, font, WHITE)
            pygame.display.flip()
            time.sleep(1)
        # Limpiar los números de la pantalla dejando solo el fondo
        animate_background()
        pygame.display.flip()

    # Inicializar variables de la animación del fondo
    bg_toggle = True  # Alterna entre los dos fotogramas
    last_frame_time = time.time()

    # Lógica del juego principal
    running = True
    reaction_time = None

    while running:
        # Animar fondo en la pantalla inicial (si es necesario agregar algo aquí)
        countdown()

        wait_time = random.uniform(2, 5)  # Espera aleatoria
        time.sleep(wait_time)

        sound.play()
        start_time = time.time()

        space_pressed = False
        while not space_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    space_pressed = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        reaction_time = time.time() - start_time
                        space_pressed = True

        time.sleep(1)  # Pausa antes de mostrar el resultado

        # Guardar el resultado en la base de datos
        nickname = "nickname"  # Reemplaza con la variable que almacena el nombre del usuario actual
        result = f"Tiempo de reacción: {reaction_time:.3f} segundos"
        save_game_result(nickname, "Game 2", result)

        # Determinar el nivel basado en el tiempo de reacción
        if reaction_time < 0.3:
            nivel = "nivel: avanzado"
        elif 0.3 <= reaction_time <= 0.8:
            nivel = "nivel: medio"
        else:
            nivel = "nivel: bajo"

        # Mostrar el resultado
        result_screen = True
        global current_frammm, frame_counter
        running = True
        start_time = time.time()  # Tiempo inicial para el cambio de imágenes

        while running:
            screen.blit(animation_framesmm[current_frammm], (0, 0))

            # Actualizar el frame de la animación
            frame_counter += 1
            if frame_counter >= frame_delaymm:
                frame_counter = 0
                current_frammm = (current_frammm + 1) % len(animation_framesmm)

            draw_text("RESULTS", screen_width // 2, screen_height // 2 - 260, fontgame1, WHITE)
            draw_text(f"Tiempo de reacción: {reaction_time:.3f} segundos", screen_width // 2, screen_height // 2 - 140, fontgame1, WHITE)
            draw_text(nivel, screen_width // 2, screen_height // 2 - 60, fontgame1, WHITE)

            # Mostrar imágenes según el nivel
            elapsed_time = time.time() - start_time
            if nivel == "nivel: bajo":
                screen.blit(estrella1azul, (screen_width // 2 - estrella1azul.get_width() // 2, screen_height // 2 + 20))
            elif nivel == "nivel: medio":
                if elapsed_time < 1.5:
                    screen.blit(estrella1azul, (screen_width // 2 - estrella1azul.get_width() // 2, screen_height // 2 + 20))
                else:
                    screen.blit(estrella2azul, (screen_width // 2 - estrella2azul.get_width() // 2, screen_height // 2 + 20))
            elif nivel == "nivel: avanzado":
                if elapsed_time < 1.5:
                    screen.blit(estrella1azul, (screen_width // 2 - estrella1azul.get_width() // 2, screen_height // 2 + 20))
                elif elapsed_time < 3:
                    screen.blit(estrella2azul, (screen_width // 2 - estrella2azul.get_width() // 2, screen_height // 2 + 20))
                else:
                    screen.blit(estrella3azul, (screen_width // 2 - estrella3azul.get_width() // 2, screen_height // 2 + 20))

            # Botón Cancel
            cancel_rect = botonca.get_rect(topleft=(60, screen_height - 230))
            screen.blit(botonazull, cancel_rect.topleft)
            mouse_pos = pygame.mouse.get_pos()  # Posición actual del mouse
            if cancel_rect.collidepoint(mouse_pos):
                draw_text("Cancel", cancel_rect.centerx, cancel_rect.centery, font, (WHITE))  # Hover
            else:
                draw_text("Cancel", cancel_rect.centerx, cancel_rect.centery, font, BLACK)  # Blanco por defecto

            # Botón Again
            again_rect = botoncaa.get_rect(topright=(screen_width - 60, screen_height - 230))
            screen.blit(botonazull, again_rect.topleft)
            if again_rect.collidepoint(mouse_pos):
                draw_text("Again", again_rect.centerx, again_rect.centery, font, (WHITE))  # Hover
            else:
                draw_text("Again", again_rect.centerx, again_rect.centery, font, BLACK)  # Blanco por defecto

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    result_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Click izquierdo
                    if cancel_rect.collidepoint(event.pos):
                        return  # Dirigir a la ventana anterior
                    elif again_rect.collidepoint(event.pos):
                        running = False
                        game2play()  # Reiniciar el juego llamando a la función

    pygame.quit()



#ventana de game2menu
def game2menu():
    global current_framm, frame_counter
    running = True
    while running:
        # Dibujar el frame actual de la animación como fondo
        screen.blit(animation_framesm[current_framm], (0, 0))

        # Actualizar el frame de la animación
        frame_counter += 1
        if frame_counter >= frame_delaym:
            frame_counter = 0
            current_framm = (current_framm + 1) % len(animation_framesm)


        # Botón "play"
        play_button_x = screen_width // 2 - botonazul.get_width() // 2
        play_button_y = screen_height // 2 - botonazul.get_height()-80
        screen.blit(botonazul, (play_button_x, play_button_y))
        play_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), play_button_x, play_button_y, botonazul.get_width(), botonazul.get_height()) else (0,0,0)
        play_text = font.render("play", True, play_text_color)
        screen.blit(play_text, (play_button_x + botonazul.get_width() // 2 - play_text.get_width() // 2,
                                   play_button_y + botonazul.get_height() // 2 - play_text.get_height() // 2))

        # Botón "instructions"
        instructions_button_x = play_button_x-25
        instructions_button_y = play_button_y + botonazulins.get_height() + 80
        screen.blit(botonazulins, (instructions_button_x, instructions_button_y))
        instructions_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), instructions_button_x, instructions_button_y, botonazulins.get_width(), botonazulins.get_height()) else (0,0,0)
        instructions_text = font.render("instructions", True, instructions_text_color)
        screen.blit(instructions_text, (instructions_button_x + botonazulins.get_width() // 2 - instructions_text.get_width() // 2,
                                       instructions_button_y + botonazulins.get_height() // 2 - instructions_text.get_height() // 2))

        # Botón "Back" para regresar a la ventana anterior
        back_button_x = screen_width // 2 - botonazull.get_width() // 2+240
        back_button_y = screen_height - botonazull.get_height() -140
        screen.blit(botonazull, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, button_image.get_width(), botonback.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonazull.get_width() // 2 - back_text.get_width() // 2,
                               back_button_y + botonazull.get_height() // 2 - back_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if is_mouse_over_button(pygame.mouse.get_pos(), play_button_x, play_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    game2play()
                elif is_mouse_over_button(pygame.mouse.get_pos(), instructions_button_x, instructions_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    game2instructions()
                elif is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    return  # Regresar a la ventana anterior

    pygame.quit()

#ventana de game3instructions
def game3instructions():
    global current_framzz, frame_counter
    running=True
    while running:
        screen.blit(animation_frameszz[current_framzz], (0, 0))

        # Actualizar el frame de la animación
        frame_counter += 1
        if frame_counter >= frame_delayzz:
            frame_counter = 0
            current_framzz = (current_framzz + 1) % len(animation_frameszz)

        tex_instructionstitle = font3.render("INSTRUCTIONS GAME 3",True,(WHITE))
        te_instructiontitle = font3.render("INSTRUCTIONS GAME 3",True,(BLACK))

        inst1 = font2.render("1.-Tras la cuenta regresiva, comenzará ",True,(BLACK))
        inst12 = font2.render("el juego.", True,(BLACK))
        inst11 = font2.render("2.-Usa las teclas de flecha de tu teclado",True,(BLACK))
        inst111 = font2.render("3.-Presiona la flecha correcta justo cuando la",True,(BLACK))
        inst1112 = font2.render("flecha que cae alcance la zona resaltada.",True,(BLACK))
        inst1111 = font2.render("4.-Solo se cuentan como correctas las teclas ",True,(BLACK))
        inst11112 = font2.render("presionadas cuando la flecha está dentro ",True,(BLACK))
        inst111122 = font2.render("de esta zona.",True,(BLACK))
        ins1 = font2.render("5.-Gana 1 punto por cada flecha correcta.",True,(BLACK))
        ins11 = font2.render("6.-Por cada error (falla o tecla incorrecta)",True,(BLACK))
        ins112 = font2.render(",sumarás un error. ",True,(BLACK))
        ins111 = font2.render("7.-Cuando acumulas 3 errores, el juego",True,(BLACK))
        ins1112 = font2.render("termina automáticamente.",True,(BLACK))
        ins1111 = font2.render("8.-Al final, podrás ver los resultados",True,(BLACK))
        ins11112 = font2.render("en la pantalla.",True,(BLACK))

        screen.blit(tex_instructionstitle,(150,55))
        screen.blit(te_instructiontitle,(145,55))
        screen.blit(inst1,(70,90))
        screen.blit(inst12,(80,115))
        screen.blit(inst11,(70,145))
        screen.blit(inst111,(70,175))
        screen.blit(inst1112,(80,205))
        screen.blit(inst1111,(70,235))
        screen.blit(inst11112,(80,265))
        screen.blit(inst111122,(80,295))
        screen.blit(ins1,(70,320))
        screen.blit(ins11,(70,355))
        screen.blit(ins112,(80,385))
        screen.blit(ins111,(70,415))
        screen.blit(ins1112,(80,445))
        screen.blit(ins1111,(70,475))
        screen.blit(ins11112,(80,505))

        # Botón "Back" para regresar a la ventana anterior
        back_button_x = screen_width // 2 - botonrosaa.get_width() // 2 + 240
        back_button_y = screen_height - botonrosaa.get_height() - 180
        screen.blit(botonrosaa, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, botonrosaa.get_width(), botonrosaa.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonrosaa.get_width() // 2 - back_text.get_width() // 2,
                                back_button_y + botonrosaa.get_height() // 2 - back_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, button_image.get_width(), button_image.get_height()):
                    return  # Regresar a la ventana anterior

    pygame.quit()

#ventana de game3play
def game3play():
    running = True

    # Cargar frames de la animación
    bg_frames = [pygame.image.load(f"bg/bg{i}.png") for i in range(1, 24)]
    current_bg_index = 0
    bg_timer = 0

    # Configuración inicial
    ARROW_KEYS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    ARROW_SYMBOLS = ["\u2191", "\u2193", "\u2190", "\u2192"]  # Flechas Unicode para cada dirección
    arrow_speed = 5
    speed_increment = 0.3  # Incremento pequeño por cada flecha procesada correctamente
    arrows = []

    # Variables del juego
    score = 0
    errors = 0
    game_over = False

    IMPACT_ZONE_Y = (screen_height // 2) - 20
    IMPACT_ZONE_HEIGHT = 95
    IMPACT_ZONE_WIDTH = 598

    def generate_arrow():
        arrow_key = random.choice(ARROW_KEYS)
        x_pos = screen_width // 2 - 20
        arrows.append({
            "key": arrow_key,
            "x": x_pos,
            "y": +40,
            "pressed": False,
            "pressed_time": None
        })

    def draw_arrows():
        for arrow in arrows:
            color = RED if arrow["pressed"] else BLACK
            text = fontflechas.render(ARROW_SYMBOLS[ARROW_KEYS.index(arrow["key"])], True, color)
            screen.blit(text, (arrow["x"], arrow["y"]))

    def display_text(text, x, y, color=BLACK):
        rendered_text = fontgame1.render(text, True, color)
        screen.blit(rendered_text, (x, y))

    def display_textt(text, x, y, color=WHITE):
        rendered_textt = font.render(text, True, color)
        screen.blit(rendered_textt, (x, y))

    def draw_impact_zone():
        impact_x = (screen_width - IMPACT_ZONE_WIDTH) // 2
        pygame.draw.rect(screen, GRAY, (impact_x, IMPACT_ZONE_Y, IMPACT_ZONE_WIDTH, IMPACT_ZONE_HEIGHT))

    def countdown():
        for i in range(3, 0, -1):
            # Actualizar fondo con la animación
            screen.blit(bg_frames[current_bg_index], (0, 0))
            display_text(str(i), screen_width // 2 - 20, screen_height // 2 - 40)
            pygame.display.flip()
            time.sleep(1)
        # Mostrar "START" sin flechas ni texto adicional
        screen.blit(bg_frames[current_bg_index], (0, 0))
        display_text("START", screen_width // 2 - 60, screen_height // 2 - 40)
        pygame.display.flip()
        time.sleep(1)

    def show_result_screen():
        global estrella1rosa, estrella2rosa, estrella3rosa
        nivel_imagenes = []

        # Determinar nivel y las imágenes correspondientes
        if score < 7:
            nivel_texto = "Nivel: Bajo"
            nivel_imagenes = [estrella1rosa]
        elif 8 <= score <= 16:
            nivel_texto = "Nivel: Medio"
            nivel_imagenes = [estrella1rosa, estrella2rosa]
        else:
            nivel_texto = "Nivel: Avanzado"
            nivel_imagenes = [estrella1rosa, estrella2rosa, estrella3rosa]

        # Mostrar la pantalla de resultados
        for imagen in nivel_imagenes:
            screen.blit(rabittsbackgroundgame, (0, 0))
            display_text("RESULTS", screen_width // 2 - 90, screen_height // 2 - 260)
            display_text(f"Tu puntuación: {score}", screen_width // 2 - 160, screen_height // 2 - 140)
            display_text(nivel_texto, screen_width // 2 - 110, screen_height // 2 - 60)

            # Mostrar la imagen correspondiente
            screen.blit(imagen, (screen_width // 2 - imagen.get_width() // 2, screen_height // 2 + 30))
            pygame.display.flip()
            time.sleep(1.5)

        while running:
            # Dibujar botones y manejar eventos
            cancel_button = pygame.Rect(55, screen_height - 185, 150, 50)
            again_button = pygame.Rect(screen_width - 145, screen_height - 185, 150, 50)
            mouse_pos = pygame.mouse.get_pos()

            screen.blit(botonrosaa, (55, screen_height - 205))
            cancel_color = (WHITE) if cancel_button.collidepoint(mouse_pos) else BLACK
            display_textt("Cancel", 55, screen_height -190, cancel_color)

            screen.blit(botonrosaa, (screen_width - 180, screen_height - 205))
            again_color = (WHITE) if again_button.collidepoint(mouse_pos) else BLACK
            display_textt("Again", screen_width - 175, screen_height - 190, again_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if cancel_button.collidepoint(event.pos):
                        return "game3menu"
                    elif again_button.collidepoint(event.pos):
                        return "restart"

            pygame.display.flip()
            pygame.time.Clock().tick(60)

    clock = pygame.time.Clock()
    arrow_timer = 0

    countdown()

    while running:
        # Actualizar frame de la animación
        bg_timer += clock.get_time()
        if bg_timer >= 300:
            current_bg_index = (current_bg_index + 1) % len(bg_frames)
            bg_timer = 0

        # Dibujar fondo animado
        screen.blit(bg_frames[current_bg_index], (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not game_over:
                for arrow in arrows:
                    if (
                        IMPACT_ZONE_Y - 20 <= arrow["y"] <= IMPACT_ZONE_Y + IMPACT_ZONE_HEIGHT + 20
                        and arrow["key"] == event.key
                    ):
                        arrow["pressed"] = True
                        arrow["pressed_time"] = pygame.time.get_ticks()
                        score += 1
                        arrow_speed += speed_increment
                        break
                else:
                    errors += 1

        if not game_over:
            arrow_timer += clock.get_time()
            if arrow_timer > 1000:
                generate_arrow()
                arrow_timer = 0

        current_time = pygame.time.get_ticks()
        for arrow in list(arrows):
            if arrow["pressed"]:
                if current_time - arrow["pressed_time"] > 300:
                    arrows.remove(arrow)
            else:
                arrow["y"] += arrow_speed
                if arrow["y"] > screen_height:
                    arrows.remove(arrow)
                    errors += 1

        draw_impact_zone()
        draw_arrows()
        display_text(f"Puntuación: {score}", 65, 90)

        if errors >= 3:
            game_over = True
            pygame.display.flip()
            time.sleep(0.5)
            result = show_result_screen()
            if result == "game3menu":
                return
            elif result == "restart":
                game3play()
                return

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



# Ventana de Game3menu
def game3menu():
    global current_framz, frame_counter
    running=True
    while running:
        screen.blit(animation_framesz[current_framz], (0, 0))

        # Actualizar el frame de la animación
        frame_counter += 1
        if frame_counter >= frame_delaym:
            frame_counter = 0
            current_framz = (current_framz + 1) % len(animation_framesz)

        # Botón "play"
        play_button_x = screen_width // 2 - botonrosa.get_width() // 2
        play_button_y = screen_height // 2 - botonrosa.get_height()-80
        screen.blit(botonrosa, (play_button_x, play_button_y))
        play_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), play_button_x, play_button_y, botonrosa.get_width(), botonrosa.get_height()) else (0,0,0)
        play_text = font.render("play", True, play_text_color)
        screen.blit(play_text, (play_button_x + botonrosa.get_width() // 2 - play_text.get_width() // 2,
                                   play_button_y + botonrosa.get_height() // 2 - play_text.get_height() // 2))

        # Botón "instructions"
        instructions_button_x = play_button_x-25
        instructions_button_y = play_button_y + botonrosains.get_height() + 80
        screen.blit(botonrosains, (instructions_button_x, instructions_button_y))
        instructions_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), instructions_button_x, instructions_button_y, botonrosains.get_width(), botonrosains.get_height()) else (0,0,0)
        instructions_text = font.render("instructions", True, instructions_text_color)
        screen.blit(instructions_text, (instructions_button_x + botonrosains.get_width() // 2 - instructions_text.get_width() // 2,
                                       instructions_button_y + botonrosains.get_height() // 2 - instructions_text.get_height() // 2))

        # Botón "Back" para regresar a la ventana anterior
        back_button_x = screen_width // 2 - botonrosaa.get_width() // 2+240
        back_button_y = screen_height - botonrosaa.get_height() -140
        screen.blit(botonrosaa, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, botonrosaa.get_width(), botonrosaa.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonrosaa.get_width() // 2 - back_text.get_width() // 2,
                               back_button_y + botonrosaa.get_height() // 2 - back_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if is_mouse_over_button(pygame.mouse.get_pos(), play_button_x, play_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    game3play()
                elif is_mouse_over_button(pygame.mouse.get_pos(), instructions_button_x, instructions_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    game3instructions()
                elif is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    return  # Regresar a la ventana anterior

    pygame.quit()


nickname = ""  # Esto debe configurarse después del inicio de sesión

#ventana de login
def login():
    # Cargar los frames de la animación
    world1 = pygame.image.load("world/world1.png")
    world2 = pygame.image.load("world/world2.png")
    animation_frames = [world1, world2]
    frame_index = 0
    frame_delay = 500  # Duración de cada frame en milisegundos
    last_frame_time = pygame.time.get_ticks()

    running = True
    while running:
            # Controlar la animación del fondo
            current_time = pygame.time.get_ticks()
            if current_time - last_frame_time > frame_delay:
                frame_index = (frame_index + 1) % len(animation_frames)
                last_frame_time = current_time

            # Dibujar el fondo animado
            screen.blit(animation_frames[frame_index], (0, 0))

            # Botón "Game 1"
            game1_button_x = screen_width // 2 - boton_game1.get_width() // 2
            game1_button_y = screen_height // 2 - boton_game1.get_height()-145
            screen.blit(boton_game1, (game1_button_x, game1_button_y))
            game1_text_color = (WHITE) if is_mouse_over_button(
                pygame.mouse.get_pos(), game1_button_x, game1_button_y, boton_game1.get_width(), boton_game1.get_height()) else (0,0,0)
            game1_text = font.render("Game 1", True, game1_text_color)
            screen.blit(game1_text, (game1_button_x + boton_game1.get_width() // 2 - game1_text.get_width() // 2,
                                    game1_button_y + boton_game1.get_height() // 2 - game1_text.get_height() // 2))

            # Botón "Game 2"
            game2_button_x = screen_width // 2 - boton_game2.get_width() // 2
            game2_button_y = screen_height // 2 - boton_game2.get_height()
            screen.blit(boton_game2, (game2_button_x, game2_button_y))
            game2_text_color = (WHITE) if is_mouse_over_button(
                pygame.mouse.get_pos(), game2_button_x, game2_button_y, boton_game2.get_width(), boton_game2.get_height()) else (0,0,0)
            game2_text = font.render("Game 2", True, game2_text_color)
            screen.blit(game2_text, (game2_button_x + boton_game2.get_width() // 2 - game2_text.get_width() // 2,
                                    game2_button_y + boton_game2.get_height() // 2 - game2_text.get_height() // 2))
            
            # Botón "Game 3"
            game3_button_x = screen_width // 2 - boton_game3.get_width() // 2
            game3_button_y = screen_height // 2 - boton_game3.get_height()+145
            screen.blit(boton_game3, (game3_button_x, game3_button_y))
            game3_text_color = (WHITE) if is_mouse_over_button(
                pygame.mouse.get_pos(), game3_button_x, game3_button_y, boton_game3.get_width(), boton_game3.get_height()) else (0,0,0)
            game3_text = font.render("Game 3", True, game3_text_color)
            screen.blit(game3_text, (game3_button_x + boton_game3.get_width() // 2 - game3_text.get_width() // 2,
                                    game3_button_y + boton_game3.get_height() // 2 - game3_text.get_height() // 2))
        
            
            # Botón "Back"
            back_button_x = screen_width // 2 - botonback.get_width() // 2 + 240
            back_button_y = screen_height - botonback.get_height() - 140
            screen.blit(botonback, (back_button_x, back_button_y))
            back_text_color = (WHITE) if is_mouse_over_button(
                pygame.mouse.get_pos(), back_button_x, back_button_y, botonback.get_width(), botonback.get_height()) else (0,0,0)
            back_text = font.render("Back", True, back_text_color)
            screen.blit(back_text, (back_button_x + botonback.get_width() // 2 - back_text.get_width() // 2,
                                    back_button_y + botonback.get_height() // 2 - back_text.get_height() // 2))
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if is_mouse_over_button(mouse_pos, game1_button_x, game1_button_y, button_games.get_width(), button_games.get_height()):
                        game1menu()
                    elif is_mouse_over_button(mouse_pos, game2_button_x, game2_button_y, button_games.get_width(), button_games.get_height()):
                        game2menu()
                    elif is_mouse_over_button(mouse_pos, game3_button_x, game3_button_y, button_games.get_width(), button_games.get_height()):
                        game3menu()
                    elif is_mouse_over_button(mouse_pos, back_button_x, back_button_y, button_image.get_width(), button_image.get_height()):
                        return
    pygame.quit()

# Ventana de inicio de sesión
def play_window():
    global nickname 
    # Variables locales inicializadas
    bgg_last_update = 0
    nickname = ""  # Campo de texto para el nombre de usuario
    password = ""  # Campo de texto para la contraseña
    active_input = None  # Indica qué campo está activo
    running = True

    text_log = font.render("Enter your account:", True, (WHITE))
    text_xlog = 70
    text_ylog = 70
    text_logi = font.render("Enter your account:", True, (BLACK))
    text_xlogi = 75
    text_ylogi = 70

    while running:
        # Actualizar animación de fondo
        current_time = pygame.time.get_ticks()
        if current_time - bgg_last_update > bgg_frame_duration:
            global bgg_index
            bgg_index = (bgg_index + 1) % len(bgg_frames)
            bgg_last_update = current_time
        screen.blit(bgg_frames[bgg_index], (0, 0))

        # Dibujar campos de texto y etiquetas
        screen.blit(text_log, (text_xlog, text_ylog))
        screen.blit(text_logi, (text_xlogi, text_ylogi))
        nickname_labe = font.render("Nickname", True, (255,255,255))
        nickname_label = font.render("Nickname", True, (0,0,0))
        screen.blit(nickname_labe,(65,190))
        screen.blit(nickname_label, (70, 190))
        nickname_box = pygame.Rect(250, 190, 300, 40)
        pygame.draw.rect(screen, (0,0,0), nickname_box, 2)
        nickname_text = font.render(nickname, True, (0,0,0))
        screen.blit(nickname_text, (nickname_box.x + 10, nickname_box.y + 5))
        password_labe = font.render("Password", True, (255,255,255))
        password_label = font.render("Password", True, (0,0,0))
        screen.blit(password_labe,(65,300))
        screen.blit(password_label, (70, 300))

        password_box = pygame.Rect(250, 300, 300, 40)
        pygame.draw.rect(screen, (0,0,0), password_box, 2)
        password_hidden = "*" * len(password)
        password_text = font.render(password_hidden, True, (0,0,0))
        screen.blit(password_text, (password_box.x + 10, password_box.y + 5))

        # Botón "Back"
        back_button_x = screen_width // 2 - botonback.get_width() // 2 + 240
        back_button_y = screen_height - botonback.get_height() - 140
        screen.blit(botonback, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, botonback.get_width(), botonback.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonback.get_width() // 2 - back_text.get_width() // 2,
                                back_button_y + botonback.get_height() // 2 - back_text.get_height() // 2))

        # Botón "Log In"
        log_button_x = 280
        log_button_y = 370
        screen.blit(button_imagen1, (log_button_x, log_button_y))
        log_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), log_button_x, log_button_y, button_imagen1.get_width(), button_imagen1.get_height()) else (0,0,0)
        log_text = font.render("Log In", True, log_text_color)
        screen.blit(log_text, (log_button_x + button_imagen1.get_width() // 2 - log_text.get_width() // 2,
                               log_button_y + button_imagen1.get_height() // 2 - log_text.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, botonback.get_width(), botonback.get_height()):
                        return  # Regresar a la ventana anterior
                    elif nickname_box.collidepoint(event.pos):
                        active_input = "nickname"
                    elif password_box.collidepoint(event.pos):
                        active_input = "password"
                    elif is_mouse_over_button(pygame.mouse.get_pos(), log_button_x, log_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                        if validate_credentials(nickname, password):
                            print("Inicio de sesión exitoso.")
                            login()  # Continuar a la siguiente ventana
                        else:
                            print("Credenciales incorrectas. Intente de nuevo.")

            elif event.type == pygame.KEYDOWN:
                if active_input == "nickname":
                    if event.key == pygame.K_BACKSPACE:
                        nickname = nickname[:-1]
                    else:
                        nickname += event.unicode
                elif active_input == "password":
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

    pygame.quit()

# Función para la ventana de "registrer"
def registrer_window():
    global frame_index, animation_timer

    nickname = ""
    password = ""
    active_input = None
    running = True
    show_saved_message = False
    saved_message_time = 0

    while running:
        # Dibujar el fondo de pantalla con la animación
        current_time = pygame.time.get_ticks()
        if current_time - animation_timer > frame_duration:
            frame_index = (frame_index + 1) % len(playregistrer_frames)
            animation_timer = current_time
        screen.blit(playregistrer_frames[frame_index], (0, 0))

        # Dibujar texto de registro
        tex_registrer = font.render("Create your account:", True, WHITE)
        tex_xregistrer = 70
        tex_yregistrer = 70
        text_registrer = font.render("Create your account:", True, BLACK)
        text_xregistrer = 75
        text_yregistrer = 70
        screen.blit(tex_registrer, (tex_xregistrer, tex_yregistrer))
        screen.blit(text_registrer, (text_xregistrer, text_yregistrer))

        # Dibujar campos de texto y etiquetas
        nicknam_label = font.render("Nickname", True, WHITE)
        nickname_label = font.render("Nickname", True, BLACK)
        screen.blit(nicknam_label, (65, 190))
        screen.blit(nickname_label, (70, 190))
        nickname_box = pygame.Rect(250, 190, 300, 40)
        pygame.draw.rect(screen, BLACK, nickname_box, 2)
        nickname_text = font.render(nickname, True, BLACK)
        screen.blit(nickname_text, (nickname_box.x + 10, nickname_box.y + 5))

        passwor_label = font.render("Password", True, WHITE)
        password_label = font.render("Password", True, BLACK)
        screen.blit(passwor_label, (65, 300))
        screen.blit(password_label, (70, 300))
        password_box = pygame.Rect(250, 300, 300, 40)
        pygame.draw.rect(screen, BLACK, password_box, 2)
        password_hidden = "*" * len(password)
        password_text = font.render(password_hidden, True, BLACK)
        screen.blit(password_text, (password_box.x + 10, password_box.y + 5))

        # Botón "Back"
        back_button_x = screen_width // 2 - botonback.get_width() // 2 + 240
        back_button_y = screen_height - botonback.get_height() - 140
        screen.blit(botonback, (back_button_x, back_button_y))
        back_text_color = WHITE if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, botonback.get_width(), botonback.get_height()) else BLACK
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonback.get_width() // 2 - back_text.get_width() // 2,
                                back_button_y + botonback.get_height() // 2 - back_text.get_height() // 2))

        # Botón "Save"
        save_button_x = 250
        save_button_y = 390
        screen.blit(button_imagen1, (save_button_x, save_button_y))
        save_text_color = WHITE if is_mouse_over_button(
            pygame.mouse.get_pos(), save_button_x, save_button_y, button_imagen1.get_width(), button_imagen1.get_height()) else BLACK
        save_text = font.render("Save", True, save_text_color)
        screen.blit(save_text, (save_button_x + button_imagen1.get_width() // 2 - save_text.get_width() // 2,
                                save_button_y + button_imagen1.get_height() // 2 - save_text.get_height() // 2))

        # Mostrar mensaje de "Account saved" si está activo
        if show_saved_message:
            message = font.render("Account saved", True, BLACK)
            screen.blit(message, (screen_width // 2 - message.get_width() // 2, screen_height // 2 - message.get_height() // 2))
            if pygame.time.get_ticks() - saved_message_time > 3000:  # Ocultar mensaje después de 3 segundos
                show_saved_message = False

        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, botonback.get_width(), botonback.get_height()):
                        return  # Regresar a la ventana anterior
                    elif nickname_box.collidepoint(event.pos):
                        active_input = "nickname"
                    elif password_box.collidepoint(event.pos):
                        active_input = "password"
                    elif is_mouse_over_button(pygame.mouse.get_pos(), save_button_x, save_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                        save_to_database(nickname, password)
                        nickname, password = "", ""  # Limpiar campos después de guardar
                        show_saved_message = True
                        saved_message_time = pygame.time.get_ticks()

            elif event.type == pygame.KEYDOWN:
                if active_input == "nickname":
                    if event.key == pygame.K_BACKSPACE:
                        nickname = nickname[:-1]
                    else:
                        nickname += event.unicode
                elif active_input == "password":
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

    pygame.quit()

# Función para "new_window"
def new_window():
    # Ruta de la carpeta donde están las imágenes
    carpeta_imagene = "bg"

    # Cargar los frames de la animación
    frames_animacio = []
    for i in range(1, 24):  # De 1 a 23
        nombre_archiv = f"bg{i}.png"
        ruta_complet = os.path.join(carpeta_imagene, nombre_archiv)
        image = pygame.image.load(ruta_complet).convert_alpha()
        frames_animacio.append(image)
    # Variables para la animación
    indice_fram = 0
    reloj = pygame.time.Clock()
    # Coordenadas de la animación
    x, y = 0,0

    running = True
    while running:
        # Actualizar el índice del frame
        indice_fram += 1
        if indice_fram >= len(frames_animacio):
            indice_fram = 0

        # Dibujar el frame actual
        ventana.fill((255, 255, 255))  # Limpiar la pantalla con blanco
        frame_actua = frames_animacio[indice_fram]
        ventana.blit(frame_actua, (x, y))


        # Botón "play"
        play_button_x = screen_width // 2 - button_imagen1.get_width() // 2
        play_button_y = screen_height // 2 - button_imagen1.get_height()-100
        screen.blit(button_imagen1, (play_button_x, play_button_y))
        play_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), play_button_x, play_button_y, button_imagen1.get_width(), button_imagen1.get_height()) else (0,0,0)
        play_text = font.render("play", True, play_text_color)
        screen.blit(play_text, (play_button_x + button_imagen1.get_width() // 2 - play_text.get_width() // 2,
                                   play_button_y + button_imagen1.get_height() // 2 - play_text.get_height() // 2))

        # Botón "registrer"
        instructions_button_x = play_button_x
        instructions_button_y = play_button_y + button_imagen1.get_height() +90
        screen.blit(button_imagen1, (instructions_button_x, instructions_button_y))
        instructions_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), instructions_button_x, instructions_button_y, button_imagen1.get_width(), button_imagen1.get_height()) else (0,0,0)
        instructions_text = font.render("registrer", True, instructions_text_color)
        screen.blit(instructions_text, (instructions_button_x + button_imagen1.get_width() // 2 - instructions_text.get_width() // 2,
                                       instructions_button_y + button_imagen1.get_height() // 2 - instructions_text.get_height() // 2))
                                       

        # Botón "Back" para regresar a la ventana anterior
        back_button_x = screen_width // 2 - botonback.get_width() // 2+240
        back_button_y = screen_height - botonback.get_height() -140
        screen.blit(botonback, (back_button_x, back_button_y))
        back_text_color = (WHITE) if is_mouse_over_button(
            pygame.mouse.get_pos(), back_button_x, back_button_y, button_image.get_width(), button_imagen1.get_height()) else (0,0,0)
        back_text = font.render("Back", True, back_text_color)
        screen.blit(back_text, (back_button_x + botonback.get_width() // 2 - back_text.get_width() // 2,
                               back_button_y + botonback.get_height() // 2 - back_text.get_height() // 2))

        pygame.display.flip()
        reloj.tick(fps)  # Limitar a 10 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if is_mouse_over_button(pygame.mouse.get_pos(), play_button_x, play_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    play_window()
                elif is_mouse_over_button(pygame.mouse.get_pos(), instructions_button_x, instructions_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    registrer_window()
                elif is_mouse_over_button(pygame.mouse.get_pos(), back_button_x, back_button_y, button_imagen1.get_width(), button_imagen1.get_height()):
                    return  # Regresar a la ventana anterior

    pygame.quit()

# Bucle principal
# Configuración de la ventana
ANCHO, ALTO = 700,700
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación con Pygame")

# Cargar los frames de la animación
carpeta_imagenes = "bgtitle"  # Ruta de la carpeta donde están las imágenes
frames_animacion = []  # Lista para almacenar los frames

# Cargar los 23 frames 
for i in range(1, 24):  # De 1 a 23
    nombre_archivo = f"bgtitle{i}.png"
    ruta_completa = os.path.join(carpeta_imagenes, nombre_archivo)
    imagen = pygame.image.load(ruta_completa).convert_alpha()  # Convertir a formato adecuado para Pygame
    # Obtener el tamaño actual de la imagen 
    ancho, alto = imagen.get_size()
    imagen_escalada = pygame.transform.scale(imagen, (ancho, alto))
    frames_animacion.append(imagen_escalada)

# Variables de animación
indice_frame = 0
reloj = pygame.time.Clock()
fps = 6  # Velocidad de la animación (frames por segundo)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            new_window()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar el índice del frame
    indice_frame += 1
    if indice_frame >= len(frames_animacion):
        indice_frame = 0

    # Dibujar el frame actual
    ventana.fill((255,255,255))  # Limpiar la pantalla con negro
    frame_actual = frames_animacion[indice_frame]
    x = (ANCHO - frame_actual.get_width()) // 2  # Centrar horizontalmente
    y = (ALTO - frame_actual.get_height()) // 2  # Centrar verticalmente
    ventana.blit(frame_actual, (x, y))  # Mostrar la imagen escalada
    screen.blit(text_surface2, (text_x2, text_y2))
    screen.blit(text_surface, (text_x1, text_y1))


    pygame.display.flip()

    # Controlar la velocidad de la animación
    reloj.tick(fps)

# Salir del programa
pygame.quit()