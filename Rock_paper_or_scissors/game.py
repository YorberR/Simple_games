#Game of rock, paper or scissors, consists of choosing one of the 
#3 options established while the computer will choose any option
#random, the condition to win is: rock > scissors > paper > rock

import tkinter as tk
import random

class GameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Piedra, Papel o Tijeras")
        self.options = ["piedra", "papel", "tijera"]
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds_to_win = 3
        self.rounds_played = 0

        # Set up initial screen
        self.label_title = tk.Label(master, text="Elige cuántas rondas para ganar:", font=('Helvetica', 14))
        self.label_title.pack(pady=10)
        
        self.entry_rounds = tk.Entry(master, font=('Helvetica', 14))
        self.entry_rounds.pack(pady=10)
        
        self.button_set_rounds = tk.Button(master, text="Empezar juego", command=self.start_game, font=('Helvetica', 14))
        self.button_set_rounds.pack(pady=10)
        
        self.label_score = tk.Label(master, text="", font=('Helvetica', 14))
        self.label_score.pack(pady=10)
        
        self.label_result = tk.Label(master, text="", font=('Helvetica', 14))
        self.label_result.pack(pady=10)
        
        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=10)
        
        self.button_rock = tk.Button(self.buttons_frame, text="Piedra", command=lambda: self.play_round("piedra"), state='disabled', font=('Helvetica', 14))
        self.button_rock.grid(row=0, column=0, padx=5)
        
        self.button_paper = tk.Button(self.buttons_frame, text="Papel", command=lambda: self.play_round("papel"), state='disabled', font=('Helvetica', 14))
        self.button_paper.grid(row=0, column=1, padx=5)
        
        self.button_scissors = tk.Button(self.buttons_frame, text="Tijera", command=lambda: self.play_round("tijera"), state='disabled', font=('Helvetica', 14))
        self.button_scissors.grid(row=0, column=2, padx=5)
        
        self.button_play_again = tk.Button(master, text="Jugar de nuevo", command=self.reset_game, state='disabled', font=('Helvetica', 14))
        self.button_play_again.pack(pady=10)

    def start_game(self):
        try:
            self.rounds_to_win = int(self.entry_rounds.get())
            self.label_title.config(text=f"Primer a {self.rounds_to_win} rondas gana")
            self.entry_rounds.pack_forget()
            self.button_set_rounds.pack_forget()
            
            self.button_rock.config(state='normal')
            self.button_paper.config(state='normal')
            self.button_scissors.config(state='normal')
            
            self.update_score()
        except ValueError:
            self.label_result.config(text="Por favor ingresa un número válido")

    def play_round(self, user_choice):
        computer_choice = random.choice(self.options)
        result = self.determine_winner(user_choice, computer_choice)

        if result == "Ganaste!":
            self.user_wins += 1
        elif result == "Perdiste!":
            self.computer_wins += 1
        
        self.rounds_played += 1
        self.update_score()

        if self.user_wins == self.rounds_to_win or self.computer_wins == self.rounds_to_win:
            self.end_game()

        self.label_result.config(text=f"Tu elección: {user_choice}, Elección de la computadora: {computer_choice}. {result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Empate!"
        elif (user_choice == "piedra" and computer_choice == "tijera") or \
             (user_choice == "papel" and computer_choice == "piedra") or \
             (user_choice == "tijera" and computer_choice == "papel"):
            return "Ganaste!"
        else:
            return "Perdiste!"

    def update_score(self):
        self.label_score.config(text=f"🤖 Computadora: {self.computer_wins} 🙋 Tú: {self.user_wins}")

    def end_game(self):
        if self.user_wins == self.rounds_to_win:
            winner = "¡Tú ganaste!"
        else:
            winner = "¡La computadora ganó!"
        
        self.label_result.config(text=winner)
        
        self.button_rock.config(state='disabled')
        self.button_paper.config(state='disabled')
        self.button_scissors.config(state='disabled')
        self.button_play_again.config(state='normal')

    def reset_game(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds_played = 0
        
        self.label_score.config(text="")
        self.label_result.config(text="")
        self.label_title.config(text="Elige cuántas rondas para ganar:")
        
        self.entry_rounds.pack(pady=10)
        self.button_set_rounds.pack(pady=10)
        
        self.button_play_again.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    game = GameApp(root)
    root.mainloop()
