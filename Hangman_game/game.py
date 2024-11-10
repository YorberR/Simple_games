#Hangman game, consists of guessing letters, 
#until they can guess the word 
#complete before you run out of attempts

import pygame
import random

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Fuente
FONT = pygame.font.Font(None, 36)
BUTTON_FONT = pygame.font.Font(None, 28)

# Palabras
word_list = ["PYTHON", "DEVELOPER", "HANGMAN", "GAME"]

class HangmanGame:
    def __init__(self):
        self.word_random = random.choice(word_list)
        self.word_list_underscores = ["_"] * len(self.word_random)
        self.lyrics_dict = {letter: [idx for idx, char in enumerate(self.word_random) if char == letter] for letter in self.word_random}
        self.attempts = 10
        self.guessed_letters = set()
        self.game_over = False

    def draw_hangman(self):
        parts = [
            (50, 150, 150, 150),  # base
            (100, 150, 100, 50),  # vertical pole
            (100, 50, 150, 50),   # horizontal pole
            (150, 50, 150, 70),   # rope
            (140, 70, 160, 90),   # head (circle)
            (150, 90, 150, 120),  # body
            (150, 100, 140, 110), # left arm
            (150, 100, 160, 110), # right arm
            (150, 120, 140, 130), # left leg
            (150, 120, 160, 130)  # right leg
        ]
        for i in range(10 - self.attempts):
            if i == 4:  # draw head
                pygame.draw.circle(screen, BLACK, (150, 80), 10, 2)
            else:
                pygame.draw.line(screen, BLACK, parts[i][:2], parts[i][2:], 2)

    def check_letter(self, letter):
        if not letter.isalpha() or letter in self.guessed_letters:
            return
        self.guessed_letters.add(letter)
        if letter in self.word_random:
            for idx in self.lyrics_dict[letter]:
                self.word_list_underscores[idx] = letter
            if "_" not in self.word_list_underscores:
                self.show_end_game_message("¡Ganaste!")
        else:
            self.attempts -= 1
            if self.attempts == 0:
                self.show_end_game_message("Perdiste")

    def show_end_game_message(self, result):
        self.game_over = True
        self.end_message = f"{result}, la palabra era {self.word_random}"
        self.render_message(self.end_message)
        self.render_buttons()

    def render_message(self, message):
        text = FONT.render(message, True, BLACK)
        screen.blit(text, (50, 250))

    def render_buttons(self):
        play_again_button = pygame.Rect(WIDTH//3 - 100, HEIGHT//2 + 50, 200, 50)
        quit_button = pygame.Rect(2*WIDTH//3 - 100, HEIGHT//2 + 50, 200, 50)
        pygame.draw.rect(screen, GREEN, play_again_button)
        pygame.draw.rect(screen, RED, quit_button)

        play_again_text = BUTTON_FONT.render("Jugar de nuevo", True, WHITE)
        quit_text = BUTTON_FONT.render("Salir", True, WHITE)

        screen.blit(play_again_text, (play_again_button.x + 25, play_again_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 75, quit_button.y + 10))

    def reset_game(self):
        self.__init__()

    def render(self):
        screen.fill(WHITE)
        self.draw_hangman()
        word_text = FONT.render(" ".join(self.word_list_underscores), True, BLACK)
        screen.blit(word_text, (50, 200))
        guessed_text = FONT.render(f"Letras utilizadas: {', '.join(sorted(self.guessed_letters))}", True, BLACK)
        screen.blit(guessed_text, (50, 300))
        if self.game_over:
            self.render_message(self.end_message)
            self.render_buttons()

def main():
    game = HangmanGame()
    running = True
    while running:
        screen.fill(WHITE)
        game.render()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not game.game_over:
                    if event.unicode.isalpha():
                        game.check_letter(event.unicode.upper())
            elif event.type == pygame.MOUSEBUTTONDOWN and game.game_over:
                mouse_pos = event.pos
                if WIDTH//3 - 100 < mouse_pos[0] < WIDTH//3 + 100 and HEIGHT//2 + 50 < mouse_pos[1] < HEIGHT//2 + 100:
                    game.reset_game()
                elif 2*WIDTH//3 - 100 < mouse_pos[0] < 2*WIDTH//3 + 100 and HEIGHT//2 + 50 < mouse_pos[1] < HEIGHT//2 + 100:
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()
