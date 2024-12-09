#Game of rock, paper or scissors, consists of choosing one of the 
#3 options established while the computer will choose any option
#random, the condition to win is: rock > scissors > paper > rock

import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piedra, Papel o Tijeras")

FONT = pygame.font.SysFont('Arial', 36)
BUTTON_FONT = pygame.font.SysFont('Arial', 28)

choices = ["Piedra", "Papel", "Tijeras"]

class GameApp:
    def __init__(self):
        self.options = ["piedra", "papel", "tijera"]
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds_to_win = 3
        self.rounds_played = 0
        self.game_over = False
        self.user_choice = None
        self.computer_choice = None
        self.result = None
        self.winner = None
        self.entry_active = False
        self.input_text = ""

    def start_game(self):
        try:
            self.rounds_to_win = int(self.input_text)
            self.entry_active = False
            self.user_choice = None
            self.computer_choice = None
            self.result = None
            self.update_screen()
        except ValueError:
            self.result = "Por favor ingresa un número válido"
            self.update_screen()

    def play_round(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(self.options)
        self.result = self.determine_winner(self.user_choice, self.computer_choice)

        if self.result == "Ganaste!":
            self.user_wins += 1
        elif self.result == "Perdiste!":
            self.computer_wins += 1
        
        self.rounds_played += 1
        self.update_screen()

        if self.user_wins == self.rounds_to_win or self.computer_wins == self.rounds_to_win:
            self.end_game()
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Empate!"
        elif (user_choice == "Piedra" and computer_choice == "Tijera") or \
            (user_choice == "Papel" and computer_choice == "Piedra") or \
            (user_choice == "Tijera" and computer_choice == "Papel"):
            return "Ganaste!"
        else:
            return "Perdiste!"

    def update_screen(self):
        screen.fill(WHITE)
        if self.entry_active:
            text = FONT.render("Elige cuántas rondas para ganar:", True, BLACK)
            screen.blit(text, (150, 100))
            entry_box = pygame.Rect(300, 200, 200, 50)
            pygame.draw.rect(screen, BLACK, entry_box, 2)
            entry_text = FONT.render(self.input_text, True, BLACK)
            screen.blit(entry_text, (entry_box.x + 10, entry_box.y + 10))
            start_button = pygame.Rect(300, 300, 200, 50)
            pygame.draw.rect(screen, GREEN, start_button)
            start_text = BUTTON_FONT.render("Empezar juego", True, WHITE)
            screen.blit(start_text, (start_button.x + 20, start_button.y + 10))
        else:
            score_text = FONT.render(f"Rondas jugadas: {self.rounds_played}, Computadora: {self.computer_wins} - Tú: {self.user_wins}", True, BLACK)
            screen.blit(score_text, (150, 50))
            if self.user_choice:
                lines = [
                    f"Tu elección: {self.user_choice}",
                    f"Elección de la computadora: {self.computer_choice}",
                    f"Resultado: {self.result}"
                ]
                y_offset = 150
                for line in lines:
                    result_text = FONT.render(line, True, BLACK)
                    screen.blit(result_text, (50, y_offset))
                    y_offset += FONT.get_height()
            if not self.game_over:
                rock_button = pygame.Rect(150, 400, 150, 50)
                paper_button = pygame.Rect(325, 400, 150, 50)
                scissors_button = pygame.Rect(500, 400, 150, 50)
                pygame.draw.rect(screen, GREEN, rock_button)
                pygame.draw.rect(screen, GREEN, paper_button)
                pygame.draw.rect(screen, GREEN, scissors_button)
                rock_text = BUTTON_FONT.render("Piedra", True, WHITE)
                paper_text = BUTTON_FONT.render("Papel", True, WHITE)
                scissors_text = BUTTON_FONT.render("Tijera", True, WHITE)
                screen.blit(rock_text, (rock_button.x + 10, rock_button.y + 10))
                screen.blit(paper_text, (paper_button.x + 10, paper_button.y + 10))
                screen.blit(scissors_text, (scissors_button.x + 10, scissors_button.y + 10))
            else:
                if self.user_wins == self.rounds_to_win:
                    winner = "¡Tú ganaste!"
                else:
                    winner = "¡La computadora ganó!"
                result_text = FONT.render(winner, True, BLACK)
                screen.blit(result_text, (50, HEIGHT - 100)) 
                play_again_button = pygame.Rect(100, 400, 200, 50)
                quit_button = pygame.Rect(325, 400, 200, 50)
                menu_button = pygame.Rect(550, 400, 200, 50)
                pygame.draw.rect(screen, GREEN, play_again_button)
                pygame.draw.rect(screen, RED, quit_button)
                pygame.draw.rect(screen, BLUE, menu_button)
                play_again_text = BUTTON_FONT.render("Jugar de nuevo", True, WHITE)
                quit_text = BUTTON_FONT.render("Salir", True, WHITE)
                menu_text = BUTTON_FONT.render("Menú", True, WHITE)
                screen.blit(play_again_text, (play_again_button.x + 25, play_again_button.y + 10))
                screen.blit(quit_text, (quit_button.x + 75, quit_button.y + 10))
                screen.blit(menu_text, (menu_button.x + 75, menu_button.y + 10))
        pygame.display.flip()

    def end_game(self):
        self.game_over = True
        self.update_screen()

    def reset_game(self):
        self.__init__()
        self.entry_active = True
        self.update_screen()

def main():
    game = GameApp()
    game.entry_active = True
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game.entry_active:
                    if event.key == pygame.K_RETURN:
                        game.start_game()
                    elif event.key == pygame.K_BACKSPACE:
                        game.input_text = game.input_text[:-1]
                    else:
                        game.input_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if game.entry_active:
                    if 300 < mouse_pos[0] < 500 and 300 < mouse_pos[1] < 350:
                        game.start_game()
                elif game.game_over:
                    if 100 < mouse_pos[0] < 300 and 400 < mouse_pos[1] < 450:
                        game.reset_game()
                    elif 325 < mouse_pos[0] < 525 and 400 < mouse_pos[1] < 450:
                        running = False
                    elif 550 < mouse_pos[0] < 750 and 400 < mouse_pos[1] < 450:
                        return
                else:
                    if 150 < mouse_pos[0] < 300 and 400 < mouse_pos[1] < 450:
                        game.play_round("Piedra")
                    elif 325 < mouse_pos[0] < 475 and 400 < mouse_pos[1] < 450:
                        game.play_round("Papel")
                    elif 500 < mouse_pos[0] < 650 and 400 < mouse_pos[1] < 450:
                        game.play_round("Tijera")

        game.update_screen()

    pygame.quit()

if __name__ == "__main__":
    main()
