import pygame, sys

WIDTH = 512
HEIGHT = 512
SCREEN_COLOR = (255,255,255)
TEXT_COLOR = (255,0,0)
LINE_COLOR = (0,0,0)

def draw_main_screen(screen):

    title_font = pygame.font.Font(None,100)

    select_font = pygame.font.Font(None,45)

    button_font = pygame.font.Font(None,30)

    screen.fill(SCREEN_COLOR)


    easy_text = button_font.render("Easy",0,SCREEN_COLOR)
    medium_text = button_font.render("Medium",0,SCREEN_COLOR)
    hard_text = button_font.render("Hard",0,SCREEN_COLOR)

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1]+20))
    easy_surface.fill(TEXT_COLOR)
    easy_surface.blit(easy_text,(10,10))

    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH//2-100,HEIGHT//2)
    )
    screen.blit(easy_surface,easy_rectangle)

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1]+20))
    medium_surface.fill(TEXT_COLOR)
    medium_surface.blit(medium_text,(10,10))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH//2,HEIGHT//2)
    )
    screen.blit(medium_surface,medium_rectangle)

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1]+20))
    hard_surface.fill(TEXT_COLOR)
    hard_surface.blit(hard_text,(10,10))

    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH//2+100,HEIGHT//2)
    )
    screen.blit(hard_surface,hard_rectangle)




    title_place = title_font.render("Sudoku",0,TEXT_COLOR)
    title_rect = title_place.get_rect(
        center=(WIDTH//2,HEIGHT//2-150))
    
    screen.blit(title_place,title_rect)

    desc_place = select_font.render("Select Game Mode:",0,TEXT_COLOR)
    desc_rect = desc_place.get_rect(
        center=(WIDTH//2,HEIGHT//2-75))

    screen.blit(desc_place,desc_rect)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30 
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()
def draw_win(screen):
    screen.fill(SCREEN_COLOR)
    title_font = pygame.font.Font(None,100)
    title_place = title_font.render("Game Won!",0,TEXT_COLOR)
    title_rect = title_place.get_rect(
        center=(WIDTH//2,HEIGHT//2-150))
    
    screen.blit(title_place,title_rect)

    button_font = pygame.font.Font(None,50)
    medium_text = button_font.render("Exit",0,SCREEN_COLOR)
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1]+20))
    medium_surface.fill(TEXT_COLOR)
    medium_surface.blit(medium_text,(10,10))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH//2,HEIGHT//2)
    )
    screen.blit(medium_surface,medium_rectangle)
def draw_lose(screen):
    screen.fill(SCREEN_COLOR)
    title_font = pygame.font.Font(None,100)
    title_place = title_font.render("Game Over",0,TEXT_COLOR)
    title_rect = title_place.get_rect(
        center=(WIDTH//2,HEIGHT//2-150))
    
    screen.blit(title_place,title_rect)

    button_font = pygame.font.Font(None,50)
    medium_text = button_font.render("Restart",0,SCREEN_COLOR)
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1]+20))
    medium_surface.fill(TEXT_COLOR)
    medium_surface.blit(medium_text,(10,10))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH//2,HEIGHT//2)
    )
    screen.blit(medium_surface,medium_rectangle)

def draw_board_screen(screen):
    game_height = HEIGHT-50
    cell = WIDTH/9 # 9x9 grid
    button_font = pygame.font.Font(None,20)

    selected_cell = None
    #Draw Lines
    def draw():
        screen.fill(SCREEN_COLOR)
        if selected_cell is not None:
            row, col = selected_cell
            pygame.draw.rect(
                screen,
                TEXT_COLOR,
                pygame.Rect(col * cell, row * game_height/9, cell, cell),
                3,
            )
        for row in range(10):
            thickness = 3 if row %3==0 else 1
            pygame.draw.line(
                screen,LINE_COLOR,(0,row*(game_height/9)),(WIDTH,row*(game_height/9)), thickness
            )
            pygame.draw.line(
                screen,LINE_COLOR,(row*cell,0),(row*cell,game_height), thickness
            )
        #Creates the buttons
        
        reset_text = button_font.render("RESET",0,SCREEN_COLOR)

        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1]+20))
        reset_surface.fill(TEXT_COLOR)
        reset_surface.blit(reset_text,(10,10))

        reset_rectangle = reset_surface.get_rect(
            center=(WIDTH//2-100,HEIGHT//2+230)
        )
        screen.blit(reset_surface,reset_rectangle)

        restart_text = button_font.render("RESTART",0,SCREEN_COLOR)

        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1]+20))
        restart_surface.fill(TEXT_COLOR)
        restart_surface.blit(restart_text,(10,10))

        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH//2,HEIGHT//2+230)
        )
        screen.blit(restart_surface,restart_rectangle)

        quit_text = button_font.render("QUIT",0,SCREEN_COLOR)

        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1]+20))
        quit_surface.fill(TEXT_COLOR)
        quit_surface.blit(quit_text,(10,10))

        quit_rectangle = quit_surface.get_rect(
            center=(WIDTH//2+100,HEIGHT//2+230)
        )
        screen.blit(quit_surface,quit_rectangle)
        return quit_rectangle,reset_rectangle,quit_rectangle
    # Loop
    while True:
        reset_rectangle, restart_rectangle, quit_rectangle = draw()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    sys.exit()
                elif reset_rectangle.collidepoint(event.pos):
                    pass # resets board
                elif restart_rectangle.collidepoint(event.pos):
                    pass # restarts game
                else:
                    x,y = event.pos
                    if x<WIDTH and y<game_height:
                        selected_cell =(y//(game_height/9),x//cell)
        pygame.display.update()
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    difficulty = draw_main_screen(screen) # Dislays the start menu and returns the number of empty cells 30,40,or 50 depending on difficulty chosen
    print(difficulty) # Number of empty cells
    draw_board_screen(screen)

if __name__=="__main__":
    main()