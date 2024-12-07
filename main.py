import pygame
import sys
from Blackjack.game import main as blackjack_main
from Hangman.game import main as hangman_main
from Rock_paper_or_scissors.game import main as rps_main

def run_game(game_main):
    game_main()
    main_menu()

def main_menu():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Menú de Juegos')

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont('Arial', 36)

    options = ["Juego 1: Blackjack", "Juego 2: Ahorcado", "Juego 3: Piedra, Papel o Tijeras", "Salir"]
    option_functions = [blackjack_main, hangman_main, rps_main, sys.exit]
    selected_option = 0

    def draw_menu():
        screen.fill(WHITE)
        for i, option in enumerate(options):
            color = BLACK if i == selected_option else (100, 100, 100)
            text = font.render(option, True, color)
            screen.blit(text, (300, 200 + i * 50))
        pygame.display.flip()

    running = True
    while running:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    run_game(option_functions[selected_option])
    
    pygame.quit()

if __name__ == "__main__":
    main_menu()
