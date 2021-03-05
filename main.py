import pygame

pygame.init()

width = 540
height = 650
square = 60

#tworzenie okna
screen = pygame.display.set_mode((width, height))

# title and icon
pygame.display.set_caption("Sudoku")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

screen.fill(("white"))
# pygame.draw.line(screen, "black", (10, 10), (300, 300), 10)

def draw_board():
    for nr_linii in range(0, 10):
        line_thickness = 2
        if nr_linii % 3 == 0:
            line_thickness = 4
        # poziome linie
        pygame.draw.line(screen, "black", (0, nr_linii*square), (width, nr_linii*square), line_thickness)
        # pionowe linie
        pygame.draw.line(screen, "black", (nr_linii * square, 0), (nr_linii * square, square*9), line_thickness)

draw_board()
#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill(("white"))
    pygame.display.update()
