import pygame, logic

WIDTH = 512
HEIGHT = 512
SCREEN_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 0, 0)
LINE_COLOR = (0, 0, 0)

GAME_HEIGHT = HEIGHT - 50
CELL_WIDTH = WIDTH / 9
CELL_HEIGHT = GAME_HEIGHT / 9


def draw_main_screen(screen):
    title_font = pygame.font.Font(None, 100)

    select_font = pygame.font.Font(None, 45)

    button_font = pygame.font.Font(None, 30)

    screen.fill(SCREEN_COLOR)

    easy_text = button_font.render("Easy", 0, SCREEN_COLOR)
    medium_text = button_font.render("Medium", 0, SCREEN_COLOR)
    hard_text = button_font.render("Hard", 0, SCREEN_COLOR)

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(TEXT_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 100, HEIGHT // 2)
    )
    screen.blit(easy_surface, easy_rectangle)

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(TEXT_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )
    screen.blit(medium_surface, medium_rectangle)

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(TEXT_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2)
    )
    screen.blit(hard_surface, hard_rectangle)

    title_place = title_font.render("Sudoku", 0, TEXT_COLOR)
    title_rect = title_place.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))

    screen.blit(title_place, title_rect)

    desc_place = select_font.render("Select Game Mode:", 0, TEXT_COLOR)
    desc_rect = desc_place.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 75))

    screen.blit(desc_place, desc_rect)

    return easy_rectangle, medium_rectangle, hard_rectangle


def draw_win(screen) -> pygame.Rect:
    screen.fill(SCREEN_COLOR)
    title_font = pygame.font.Font(None, 100)
    title_place = title_font.render("Game Won!", 0, TEXT_COLOR)
    title_rect = title_place.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))

    screen.blit(title_place, title_rect)

    button_font = pygame.font.Font(None, 50)
    medium_text = button_font.render("Exit", 0, SCREEN_COLOR)
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(TEXT_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )
    screen.blit(medium_surface, medium_rectangle)

    return medium_rectangle


def draw_lose(screen) -> pygame.Rect:
    screen.fill(SCREEN_COLOR)
    title_font = pygame.font.Font(None, 100)
    title_place = title_font.render("Game Over :(", 0, TEXT_COLOR)
    title_rect = title_place.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150)
    )
    screen.blit(title_place, title_rect)

    button_font = pygame.font.Font(None, 50)
    medium_text = button_font.render("Restart", 0, SCREEN_COLOR)
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(TEXT_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )
    screen.blit(medium_surface, medium_rectangle)
    return medium_rectangle


def draw_board_screen(screen, board: logic.Board, selected_cell) -> tuple[pygame.Rect, pygame.Rect, pygame.Rect]:
    button_font = pygame.font.Font(None, 20)
    cell_number_font = pygame.font.Font(None, 50)
    cell_number_sketch_font = pygame.font.Font(None, 35)

    screen.fill(SCREEN_COLOR)
    for row in range(10):
        thickness = 3 if row % 3 == 0 else 1
        pygame.draw.line(
            screen, LINE_COLOR, (0, row * CELL_HEIGHT), (WIDTH, row * CELL_HEIGHT), thickness
        )
        pygame.draw.line(
            screen, LINE_COLOR, (row * CELL_WIDTH, 0), (row * CELL_WIDTH, GAME_HEIGHT), thickness
        )
    if selected_cell is not None:
        row, col = selected_cell
        pygame.draw.line(
            screen, TEXT_COLOR, (col * CELL_WIDTH, row * CELL_HEIGHT), ((col + 1) * CELL_WIDTH, row * CELL_HEIGHT), 3
        )
        pygame.draw.line(
            screen, TEXT_COLOR, (col * CELL_WIDTH, (row + 1) * CELL_HEIGHT),
            ((col + 1) * CELL_WIDTH, (row + 1) * CELL_HEIGHT), 3
        )
        pygame.draw.line(
            screen, TEXT_COLOR, (col * CELL_WIDTH, row * CELL_HEIGHT), (col * CELL_WIDTH, (row + 1) * CELL_HEIGHT), 3
        )
        pygame.draw.line(
            screen, TEXT_COLOR, ((col + 1) * CELL_WIDTH, row * CELL_HEIGHT),
            ((col + 1) * CELL_WIDTH, (row + 1) * CELL_HEIGHT), 3
        )

    # Render the cell values
    for row in range(len(board.current_board)):
        for col in range(len(board.current_board)):
            if board.current_board[row][col].get() != 0:
                cell_text = cell_number_font.render(str(board.current_board[row][col].get()), 0, LINE_COLOR)
                cell_surface = pygame.Surface((cell_text.get_size()[0], cell_text.get_size()[1]))
                cell_surface.fill(SCREEN_COLOR)
                cell_surface.blit(cell_text, (0, 0))
                screen.blit(cell_surface, cell_surface.get_rect(
                    center=((col + 0.5) * CELL_WIDTH, (row + 0.5) * CELL_HEIGHT)
                ))
            elif board.current_board[row][col].get_sketched() != 0:
                cell_text = cell_number_sketch_font.render(str(board.current_board[row][col].get_sketched()), 0,
                                                           (100, 100, 100))
                cell_surface = pygame.Surface((cell_text.get_size()[0], cell_text.get_size()[1]))
                cell_surface.fill(SCREEN_COLOR)
                cell_surface.blit(cell_text, (0, 0))
                screen.blit(cell_surface, cell_surface.get_rect(
                    center=((col + 0.2) * CELL_WIDTH, (row + 0.3) * CELL_HEIGHT)
                ))
    # Creates the buttons
    reset_text = button_font.render("RESET", 0, SCREEN_COLOR)

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(TEXT_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 100, HEIGHT // 2 + 230)
    )
    screen.blit(reset_surface, reset_rectangle)

    restart_text = button_font.render("RESTART", 0, SCREEN_COLOR)

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(TEXT_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 230)
    )
    screen.blit(restart_surface, restart_rectangle)

    quit_text = button_font.render("QUIT", 0, SCREEN_COLOR)

    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(TEXT_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2 + 230)
    )
    screen.blit(quit_surface, quit_rectangle)
    return reset_rectangle, restart_rectangle, quit_rectangle


def init_pygame() -> pygame.Surface:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    return screen