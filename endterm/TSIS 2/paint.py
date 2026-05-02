import pygame
import sys
from datetime import datetime
from tools import draw_shape, flood_fill

# pygame-ді іске қосамыз
pygame.init()

# экранның биіктігі мен енін береміз
WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 90

# дисплейді жасаймыз
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

# сызу аймағы панель инструменттерінің астында орналасу керек
CANVAS_RECT = pygame.Rect(0, TOOLBAR_HEIGHT,WIDTH,HEIGHT-TOOLBAR_HEIGHT)

# сурет салынатын қағазды жасаймыз
canvas = pygame.Surface((WIDTH,HEIGHT-TOOLBAR_HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
LIGHT_BLUE = (180, 210, 255)

# пайдаланушыға қолжетімді түстер
colors = [
    BLACK,
    (255, 0, 0), #red
    (0, 180, 0), #green
    (0, 0, 255), #blue
    (255, 255, 0), #yellow
    (255, 120, 0), #orange
    (160, 0, 200), #purple
    WHITE
]

# шрифттар
font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 16)
text_font = pygame.font.SysFont("Arial", 28)

# программаның жағдайы
current_color = BLACK
brush_size = 5
current_tool = "pencil"

drawing = False
start_pos = None
last_pos = None

text_mode = False
text_pos = None
text_input = ""

tool_buttons = {}
color_buttons = []

#толық экранның координатасын canvas-тың координатасына ауыстырамыз
def canvas_pos(pos):
    return pos[0], pos[1] - TOOLBAR_HEIGHT

#тінтуір canvas-тың ішіндема тексереміз
def inside_canvas(pos):
    return CANVAS_RECT.collidepoint(pos)

#аспаптардың батырмаларын сызамыз
def draw_button(rect, label, active=False):
    button_color = LIGHT_BLUE if active else GRAY

    pygame.draw.rect(screen, button_color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    text = small_font.render(label, True, BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

# жоғарғы панель-ді аспаптар және түстерімен сызамыз
def draw_toolbar():
    global tool_buttons, color_buttons

    tool_buttons = {}
    color_buttons = []

    pygame.draw.rect(screen, (235, 235, 235),(0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, BLACK, (0, TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT), 2)

    # аспаптар тізімі
    tools = [
        ("pencil", "Pencil"),
        ("line", "Line"),
        ("rect", "Rect"),
        ("circle", "circle"),
        ("square", "Square"),
        ("right_triangle", "R-Tri"),
        ("eq_triangle", "E1-Tri"),
        ("rhombus", "Rhombus"),
        ("eraser", "Eraser"),
        ("fill", "Fill"),
        ("text", "Text"),
    ]

    x = 10
    y = 10
    button_width = 78
    button_height = 30

    # аспаптардың батырмаларын жасаймыз
    for tool_name, label in tools:
        rect = pygame.Rect(x, y, button_width, button_height)
        draw_button(rect, label, current_tool == tool_name)
        tool_buttons[tool_name] = rect
        x += button_width + 6

    x = 10
    y = 52

    # түстерге арналан батырмаларды жасаймыз
    for color in colors:
        rect = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

        #таңдалған түсті көрсетеді
        if color == current_color:
            pygame.draw.rect(screen, (0, 0, 0), rect, 4)

        color_buttons.append((rect, color))
        x += 38

    # ағымдағы қаріп размерін көрсетеді
    size_text = font.render(
        f"Brush: {brush_size}px | 1=small 2=medium 3=large | Ctrl+S=Save",
        True,
        BLACK
    )
    screen.blit(size_text, (350, 55))

#PNG-файл түрінде canvas-ты сақтаймыз
def save_canvas():
    filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
    pygame.image.save(canvas, filename)
    print(f"Saved as {filename}")


def draw_text_preview():
    if text_mode and text_pos is not None:
        preview = text_font.render(text_input + "|", True, current_color)
        screen.blit(preview, (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT))

def handle_toolbar_click(pos):
    global current_tool, current_color
    global text_mode, text_input, text_pos

    for tool_name, rect in tool_buttons.items():
        if rect.collidepoint(pos):
            current_tool = tool_name
            text_mode = False
            text_input = ""
            text_pos = None
            return True
    
    for rect, color in color_buttons:
        if rect.collidepoint(pos):
            current_color = color
            return True
    return False

# ЕҢ БАСТЫ ЦИКЛ

running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))
    draw_toolbar()

    # Тінтуірді сүйреген кезде сызба мен сызықты алдын ала қарау
    if drawing and start_pos is not None:
        mouse_pos = pygame.mouse.get_pos()

        if inside_canvas(mouse_pos):
            end_pos = canvas_pos(mouse_pos)
            preview_surface = screen.copy()

            if current_tool == "line":
                pygame.draw.line(
                    preview_surface,
                    current_color,
                    (start_pos[0], start_pos[1] + TOOLBAR_HEIGHT),
                    mouse_pos,
                    brush_size
                )
            elif current_tool in [
                "rect",
                "circle",
                "square",
                "right_triangle",
                "eq_triangle",
                "rhombus"
            ]:
                shape_preview = pygame.Surface(canvas.get_size(), pygame.SRCALPHA)
                draw_shape(
                    shape_preview,
                    current_tool,
                    start_pos,
                    end_pos,
                    current_color,
                    brush_size
                )
                preview_surface.blit(shape_preview, (0,TOOLBAR_HEIGHT))
            screen.blit(preview_surface, (0, 0))
    draw_text_preview()

    # pygame оқиғаларын басқарамыз
    for event in pygame.event.get():
        # терезені жабу
        if event.type == pygame.QUIT:
            running = False

        # клавиатураны өңдеу
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            # Ctrl+S арқылы сақтаймыз
            if event.key == pygame.K_s and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
                save_canvas()

            # Қаріп өлшемдері
            elif event.key == pygame.K_1:
                brush_size = 2
            
            elif event.key == pygame.K_2:
                brush_size = 5

            elif event.key == pygame.K_3:
                brush_size = 10

            # Мәтінді енгізу
            if text_mode:
                if event.key == pygame.K_RETURN:
                    final_text = text_font.render(text_input, True, current_color)
                    canvas.blit(final_text, text_pos)

                    text_mode = False
                    text_pos = None
                    text_input = ""

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_pos = None
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                
                else:
                    text_input += event.unicode
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if handle_toolbar_click(pos):
                continue

            if inside_canvas(pos):
                cpos = canvas_pos(pos)

                if current_tool == "fill":
                    flood_fill(canvas, cpos, current_color)

                elif current_tool == "text":
                    text_mode = True
                    text_pos = cpos
                    text_input = ""

                else:
                    drawing = True
                    start_pos = cpos
                    last_pos = cpos

        
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()

            if drawing and inside_canvas(pos):
                cpos = canvas_pos(pos)


                if current_tool == "pencil":
                    pygame.draw.line(canvas, current_color, last_pos, cpos, brush_size)
                    last_pos = cpos

                elif current_tool == "eraser":
                    pygame.draw.line(canvas, WHITE, last_pos, cpos, brush_size)
                    last_pos = cpos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if drawing and inside_canvas(pos):
                end_pos = canvas_pos(pos)

                if current_tool == "line":
                    pygame.draw.line(canvas, current_color, start_pos, end_pos, brush_size)

                elif current_tool in [
                    "rect",
                    "circle",
                    "square",
                    "right_triangle",
                    "eq_triangle",
                    "rhombus"
                ]:
                    draw_shape(
                        canvas,
                        current_tool,
                        start_pos,
                        end_pos,
                        current_color,
                        brush_size
                    )
            
            drawing = False
            start_pos = None
            last_pos = None
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()
