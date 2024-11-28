import visuals
import pygame
import sys

def main():
    screen = visuals.init_pygame()
    difficulty = None

    # Difficulty Selection Screen
    while difficulty == None:
        easy_rectangle, medium_rectangle, hard_rectangle = visuals.draw_main_screen(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = 40
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
        pygame.display.update()

    print(difficulty) # Number of empty cells

    selected_cell = None

    # Loop
    while True:
        reset_rectangle, restart_rectangle, quit_rectangle = visuals.draw_board_screen(screen, selected_cell)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    sys.exit()
                elif reset_rectangle.collidepoint(event.pos):
                    pass # resets board
                elif restart_rectangle.collidepoint(event.pos):
                    pass # restarts game
                else:
                    x, y = event.pos
                    if x < visuals.WIDTH and y < visuals.GAME_HEIGHT:
                        selected_cell = (y // visuals.CELL_HEIGHT, x // visuals.CELL_WIDTH)
        pygame.display.update()

if __name__ == "__main__":
    main()