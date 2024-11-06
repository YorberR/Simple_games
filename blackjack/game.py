#El Blackjack, es un juego de cartas, propio de los casinos con una
#o más barajas inglesas de 52 cartas sin los comodines, que consiste
#en sumar un valor lo más próximo a 21 pero sin pasarse. 
#En un casino cada jugador de la mesa juega únicamente contra el crupier,
#intentando conseguir una mejor jugada que este. El crupier está sujeto a
#reglas fijas que le impiden tomar decisiones sobre el juego. Por ejemplo, 
#está obligado a pedir carta siempre que su puntuación sume 16 o menos, y 
#obligado a plantarse si suma 17 o más. Las cartas numéricas suman su valor,
#las figuras suman 10 y el As vale 11 o 1, a elección del jugador. En el caso 
#del crupier, los Ases valen 11 mientras no se pase de 21, y 1 en caso contrario.
#La mejor jugada es conseguir 21 con solo dos cartas, esto es con un As más carta de valor 10.
#Esta jugada se conoce como Blackjack o 21 natural. Un Blackjack gana sobre un 21 
#conseguido con más de dos cartas. 

import random
import os

def deck_of_cards():
    DoC = []
    numbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    pints = ["♣", "♠", "♥", "♦"]
    for pint in pints:
        for number in numbers:
            card = "{}{}".format(number, pint)
            DoC.append(card)
    return DoC

def start(mallet):
    user = []
    for i in range(2):
        passed = random.choice(mallet)
        mallet.remove(passed)
        user.append(passed)
    return user

def crupiers(mallet):
    crupier = []
    for i in range(2):
        passed = random.choice(mallet)
        mallet.remove(passed)
        crupier.append(passed)
    return crupier

def card_value(card):
    if card[0] in ['K', 'Q', 'J', '1']:
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
        return "Ganaste!"
    elif user_score < crupier_score:
        return "Perdiste."
    else:
        return "Empate."

def run():
    mallet = deck_of_cards()
    user = start(mallet)
    crupier = crupiers(mallet)
    print("Cartas del crupier:", crupier[0], "y _")
    print("Tus cartas:", user)
    
    while hand_value(user) < 21:
        option = input("Elige la opción que quieres hacer: 1) Agarrar otra carta 2) Quedarse: ")
        
        if option == "1":
            passed = random.choice(mallet)
            mallet.remove(passed)
            user.append(passed)
            print("Tus cartas:", user)
        elif option == "2":
            break
        else:
            print("Opción no válida")
    
    user_score = hand_value(user)
    crupier = crupier_play(crupier, mallet)
    crupier_score = hand_value(crupier)
    
    print("Cartas del crupier:", crupier)
    print("Tus cartas:", user)
    print(ganador(user_score, crupier_score))

if __name__ == "__main__":
    run()
