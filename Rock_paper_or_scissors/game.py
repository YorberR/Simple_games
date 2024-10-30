#Game of rock, paper or scissors, consists of choosing one of the 
#3 options established while the computer will choose any option
#random, the condition to win is: rock > scissors > paper > rock

import random
import os
import time

options = ["piedra", "papel", "tijera"]
user_wins = 0
computer_wins = 0

def show_score(computer_wins, user_wins):
    print('*' * 10)
    print('Puntajes')
    print(f'''
    🤖 Computer wins: {computer_wins}
    🙋 User wins: {user_wins}
    ''')
    print('*' * 10)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == "piedra" and computer_choice == "tijera") or \
        (user_choice == "papel" and computer_choice == "piedra") or \
        (user_choice == "tijera" and computer_choice == "papel"):  

        return "Ganaste!"
    else:
        return "Perdiste!"

def show_round_result(user_choice, computer_choice):
    result = determine_winner(user_choice, computer_choice)
    if result == "Ganaste!":
        global user_wins
        user_wins += 1
    elif result == "Perdiste!":
        global computer_wins
        computer_wins += 1
    print('-' * 10)
    print("Tu elección:", user_choice)
    print("Elección de la computadora:", computer_choice)
    print('-' * 10)
    print(result)
    print("Puntuación actual: Tú", user_wins, "Computadora", computer_wins)
    return user_wins, computer_wins

def determine_game_winner(user_wins, computer_wins):
    if computer_wins == 3:
        print(f'🎖️ El ganador es Computer con {computer_wins} puntos 🎖️')
        return 'Computer'
    elif user_wins == 3:
        print(f'🎖️ El ganador es User con {user_wins} puntos 🎖️')
        return 'User'
    else:
        return None

def run(options, user_wins, computer_wins):
    while True:
        time.sleep(4)
        os.system("clear")
        show_score(computer_wins, user_wins)
        print("Puedes escribir directamente tu opción o poner el número de tu opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        user_choice = input("Elige: ").lower()

        # Convertir número a opción si es necesario
        if user_choice in ["1", "2", "3"]:
            user_choice = options[int(user_choice) - 1]

        if user_choice in options:
            computer_choice = random.choice(options)
            user_wins, computer_wins = show_round_result(user_choice, computer_choice)
            winner = determine_game_winner(user_wins, computer_wins)
            if winner:
                print(f"¡{winner} ha ganado el juego!")
                break
        else:
            print("Opción no válida, por favor elige piedra, papel o tijeras (o su número correspondiente).")

        # Preguntar si desea jugar de nuevo
        play_again = input("¿Quieres jugar otra partida? (si o no): ").lower()
        if play_again != 'si':
            print("¡Gracias por jugar!")
            break

        # Reiniciar variables para una nueva partida
        user_wins = 0
        computer_wins = 0

if __name__ == "__main__":
    run(options, user_wins, computer_wins)