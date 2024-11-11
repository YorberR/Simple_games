#Blackjack is a card game, typical of casinos with a
#or more English decks of 52 cards without the jokers, which consists
#in adding a value that is closest to 21 but without going over. 
#In a casino each player at the table plays only against the dealer,
#trying to get a better play than this. The dealer is subject to
#fixed rules that prevent you from making decisions about the game. For example, 
#you are obliged to draw a card whenever your score adds up to 16 or less, and 
#forced to stand if the score is 17 or more. The number cards add their value,
#The figures add up to 10 and the Ace is worth 11 or 1, at the player's choice. In the case 
#from the dealer, Aces are worth 11 as long as it does not go over 21, and 1 otherwise.
#The best play is to get 21 with only two cards, this is with an Ace plus a card of value 10.
#This play is known as Blackjack or natural 21. A Blackjack wins on a 21 
#achieved with more than two cards.

import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

FONT = pygame.font.SysFont('Arial', 36)
BUTTON_FONT = pygame.font.SysFont('Arial', 28)

def deck_of_cards():
    DoC = []
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["♣", "♠", "♥", "♦"]
    for suit in suits:
        for number in numbers:
            card = f"{number}{suit}"
            DoC.append(card)
    return DoC

def start(mallet):
    user = []
    for _ in range(2):
        passed = random.choice(mallet)
        mallet.remove(passed)
        user.append(passed)
    return user

def crupiers(mallet):
    crupier = []
    for _ in range(2):
        passed = random.choice(mallet)
        mallet.remove(passed)
        crupier.append(passed)
    return crupier

def card_value(card):
    if card[:-1] in ['K', 'Q', 'J', '10']:
        return 10
    elif card[0] == 'A':
        return 11
    else:
        return int(card[:-1])

def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def crupier_play(crupier, mallet):
    while hand_value(crupier) < 17:
        passed = random.choice(mallet)
        mallet.remove(passed)
        crupier.append(passed)
    return crupier

def ganador(user_score, crupier_score):
    if user_score > 21:
        return "Te pasaste de 21, perdiste."
    elif crupier_score > 21 or user_score > crupier_score:
        return "¡Ganaste!"
    elif user_score < crupier_score:
        return "Perdiste."
    else:
        return "Empate."

def render_text(text, position):
    rendered_text = FONT.render(text, True, BLACK)
    screen.blit(rendered_text, position)

def draw_buttons(game_over):
    buttons = {}
    if not game_over:
        hit_button = pygame.Rect(WIDTH // 3 - 100, HEIGHT - 100, 200, 50)
        stand_button = pygame.Rect(2 * WIDTH // 3 - 100, HEIGHT - 100, 200, 50)

        pygame.draw.rect(screen, GREEN, hit_button)
        pygame.draw.rect(screen, RED, stand_button)

        hit_text = BUTTON_FONT.render("Pedir carta", True, WHITE)
        stand_text = BUTTON_FONT.render("Quedarse", True, WHITE)

        screen.blit(hit_text, (hit_button.x + 30, hit_button.y + 10))
        screen.blit(stand_text, (stand_button.x + 40, stand_button.y + 10))

        buttons['hit'] = hit_button
        buttons['stand'] = stand_button
    else:
        play_again_button = pygame.Rect(WIDTH // 3 - 100, HEIGHT // 2 + 50, 200, 50)
        quit_button = pygame.Rect(2 * WIDTH // 3 - 100, HEIGHT // 2 + 50, 200, 50)

        pygame.draw.rect(screen, GREEN, play_again_button)
        pygame.draw.rect(screen, RED, quit_button)

        play_again_text = BUTTON_FONT.render("Jugar de nuevo", True, WHITE)
        quit_text = BUTTON_FONT.render("Salir", True, WHITE)

        screen.blit(play_again_text, (play_again_button.x + 25, play_again_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 75, quit_button.y + 10))

        buttons['play_again'] = play_again_button
        buttons['quit'] = quit_button

    return buttons

def main():
    mallet = deck_of_cards()
    user = start(mallet)
    crupier = crupiers(mallet)

    running = True
    game_over = False

    while running:
        screen.fill(WHITE)
        render_text(f"Cartas del crupier: {crupier[0]} y _", (50, 50))
        render_text(f"Tus cartas: {', '.join(user)}", (50, 100))

        if game_over:
            render_text(ganador(hand_value(user), hand_value(crupier)), (50, 150))

        buttons = draw_buttons(game_over)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if not game_over:
                    if buttons['hit'].collidepoint(mouse_pos):
                        passed = random.choice(mallet)
                        mallet.remove(passed)
                        user.append(passed)
                        if hand_value(user) >= 21:
                            crupier = crupier_play(crupier, mallet)
                            game_over = True
                    elif buttons['stand'].collidepoint(mouse_pos):
                        crupier = crupier_play(crupier, mallet)
                        game_over = True
                else:
                    if buttons['play_again'].collidepoint(mouse_pos):
                        mallet = deck_of_cards()
                        user = start(mallet)
                        crupier = crupiers(mallet)
                        game_over = False
                    elif buttons['quit'].collidepoint(mouse_pos):
                        running = False

        if game_over:
            render_text(f"Cartas del crupier: {', '.join(crupier)}", (50, 50))
            render_text(f"Tus cartas: {', '.join(user)}", (50, 100))
            pygame.display.flip()
            pygame.time.wait(2000)

    pygame.quit()

if __name__ == "__main__":
    main()
