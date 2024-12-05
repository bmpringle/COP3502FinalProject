import visuals
import pygame
import sys
import logic

def select_difficulty(screen) -> int:
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
    return difficulty

def end_screen(screen, won ):
    if won == logic.BoardCompletionState.WON:
        won = True
        "ganhou"
    elif won == logic.BoardCompletionState.LOST:
        won = False
        print("perdeu")
    else:
        print("Deu merda aqui")
    while True:
        end_screen_button = visuals.draw_win(screen) if won else visuals.draw_lose(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if end_screen_button.collidepoint(event.pos):
                    return not won
        pygame.display.update()

# Returns whether or not to play another game
def play_sudoku_game(screen, difficulty) -> bool:
    selected_cell = None

    solved_board = logic.generate_sudoku(9, difficulty)
    print("antes",solved_board[0])
    starting_board = logic.get_starting_board(solved_board[1])
    print("depois",solved_board[0])

    board = logic.Board(starting_board, solved_board[0])

    number_key_map = {
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
                    return False
                elif reset_rectangle.collidepoint(event.pos):
                    board = logic.Board(starting_board, solved_board[0])
                elif restart_rectangle.collidepoint(event.pos):
                    return True
                else:
                    x, y = event.pos
                    if x < visuals.WIDTH and y < visuals.GAME_HEIGHT:
                        selected_cell = [y // visuals.CELL_HEIGHT, x // visuals.CELL_WIDTH]
            elif event.type == pygame.KEYDOWN:
                if event.key in number_key_map:
                    board.sketch_value_in_cell(number_key_map[event.key], int(selected_cell[0]), int(selected_cell[1]))
                if event.key == pygame.K_RETURN:
                    board.confirm_sketch(int(selected_cell[0]), int(selected_cell[1]))
                    state = board.game_complete()
                    if state != logic.BoardCompletionState.INCOMPLETE:
                        return end_screen(screen, state)
                if event.key == pygame.K_LEFT:
                    if selected_cell[1] - 1 >= 0:
                        selected_cell[1] -= 1
                if event.key == pygame.K_RIGHT:
                    if selected_cell[1] + 1 < 9:
                        selected_cell[1] += 1
                if event.key == pygame.K_UP:
                    if selected_cell[0] - 1 >= 0:
                        selected_cell[0] -= 1
                if event.key == pygame.K_DOWN:
                    if selected_cell[0] + 1 < 9:
                        selected_cell[0] += 1
                    
        pygame.display.update()

def main():
    screen = visuals.init_pygame()
    should_play_again = True

    while should_play_again:
        difficulty = select_difficulty(screen)
        should_play_again = play_sudoku_game(screen, difficulty)

    

if __name__ == "__main__":
    main()