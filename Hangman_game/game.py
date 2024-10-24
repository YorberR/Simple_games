#Hangman game, consists of guessing letters, 
#until they can guess the word 
#complete before you run out of attempts

import random
import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  

def read(info="/Users/Yorber/Documents/Proyectos/Proyectos_Python/Games/Hangman_game/DATA/DATA.txt"):
    words = []
    with open(info, "r") as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def run():
    while True:
        data = read(info="/Users/Yorber/Documents/Proyectos/Proyectos_Python/Games/Hangman_game/DATA/DATA.txt")  

        word_random = random.choice(data)
        word_list = [letter for letter in word_random]
        word_list_underscores = ["_"] * len(word_list)

        lyrics_dict = {}
        for idx, letter in enumerate(word_random):
            if not lyrics_dict.get(letter):
                lyrics_dict[letter] = []
                lyrics_dict[letter].append(idx)

        attempts = 10
        guessed_letters = set()

        while attempts > 0:
            # clear_console()
            print("Adivina la palabra")
            for element in word_list_underscores:
                print(element + " ", end="")
            print("\n")

            guess = input("Ingresa una letra: ").strip().upper()

            if not guess.isalpha():
                print("Solo puedes ingresar letras.")
                continue

            if guess in guessed_letters:
                print("Ya has ingresado esa letra.")
                continue

            guessed_letters.add(guess)

            if guess in word_list:
                for idx in lyrics_dict[guess]:
                    word_list_underscores[idx] = guess
                if "_" not in word_list_underscores:
                    clear_console()
                    print("Ganaste, la palabra era", word_random)
                    break
            else:
                attempts -= 1
                print("Letra incorrecta. Intentos restantes:", attempts)

        if attempts == 0:
            clear_console()
            print("Perdiste, la palabra era", word_random)

        while True:
            jugar_de_nuevo = input("¿Quieres jugar otra vez? (si o no): ").lower()
            if jugar_de_nuevo == 'si':
                break
            elif jugar_de_nuevo == 'no':
                print("¡Hasta luego!")
                return
            else:
                print("Por favor, ingresa 's' para jugar de nuevo o 'n' para salir.")

if __name__ == "__main__":
    run()
