import gameOfLife as g
import pygame
from itertools import product


def update_view(display, surface):
    display.blit(surface, (0, 0))
    pygame.display.flip()

pygame.init()

width = 100
height = 100

window_size = (800, 800)

cell_width = window_size[0] // width
cell_height = window_size[1] // height

game_window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test Game!!")

white = (255, 255, 255)
black = (0, 0, 0)

background = pygame.Surface(game_window.get_size()).convert()
background.fill(white)

for i in range(1, width):
    pygame.draw.line(background, black, (cell_width * i, 0), (cell_width * i, window_size[0]), 1)

for i in range(1, height):
    pygame.draw.line(background, black, (0, cell_height * i), (window_size[1], cell_height * i), 1)

pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

game = g.GameOfLife()

run_program = True
run_game = False
while run_program:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run_program = False
        elif event.type is pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            block_x, block_y = mouse_x // cell_width, mouse_y // cell_height
            game.set_alive(block_x, block_y)
            pygame.draw.rect(background, black, (block_x * cell_width, block_y * cell_height, cell_width, cell_height))
        elif event.type is pygame.KEYDOWN:
            run_game = not run_game
        elif event.type is pygame.USEREVENT + 1:
            if run_game:
                for x, y in product(range(0, width + 1), range(0, height + 1)):
                    if game.is_alive(x, y):
                        pygame.draw.rect(background, black, (x * cell_width, y * cell_height, cell_width, cell_height))
                    else:
                        pygame.draw.rect(background, white, (x * cell_width, y * cell_height, cell_width, cell_height))
                game.tick()

    update_view(game_window, background)
