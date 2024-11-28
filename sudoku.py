import visuals
import pygame
import sys
import logic

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

    board = logic.Board(*logic.generate_sudoku(9, difficulty))

    key_map = {
        pygame.K_1 : 1, pygame.K_2 : 2, pygame.K_3 : 3, 
        pygame.K_4 : 4, pygame.K_5 : 5, pygame.K_6 : 6, 
        pygame.K_7 : 7, pygame.K_8 : 8, pygame.K_9 : 9
    }

    # Loop
    while True:
        reset_rectangle, restart_rectangle, quit_rectangle = visuals.draw_board_screen(screen, board, selected_cell)

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
            elif event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    board.sketch_value_in_cell(key_map[event.key], int(selected_cell[0]), int(selected_cell[1]))
                if event.key == pygame.K_RETURN:
                    board.confirm_sketch(int(selected_cell[0]), int(selected_cell[1]))
        pygame.display.update()

if __name__ == "__main__":
    main()