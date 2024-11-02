#Hangman game, consists of guessing letters, 
#until they can guess the word 
#complete before you run out of attempts

import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.word_list = self.read("./DATA/DATA.txt")
        self.word_random = random.choice(self.word_list)
        self.word_list_underscores = ["_"] * len(self.word_random)
        self.lyrics_dict = {}
        for idx, letter in enumerate(self.word_random):
            if not self.lyrics_dict.get(letter):
                self.lyrics_dict[letter] = []
            self.lyrics_dict[letter].append(idx)
        self.attempts = 10
        self.guessed_letters = set()

        self.canvas = tk.Canvas(self.master, width=200, height=200)
        self.canvas.pack(pady=20)
        self.label_word = tk.Label(self.master, text=" ".join(self.word_list_underscores), font=('Helvetica', 18))
        self.label_word.pack(pady=20)
        self.entry_letter = tk.Entry(self.master, font=('Helvetica', 14))
        self.entry_letter.pack(pady=10)
        self.button_check = tk.Button(self.master, text="Probar", command=self.check_letter)
        self.button_check.pack(pady=10)
        self.label_message = tk.Label(self.master, text="", font=('Helvetica', 14))
        self.label_message.pack(pady=20)
        self.label_guessed = tk.Label(self.master, text="Letras utilizadas: ", font=('Helvetica', 14))
        self.label_guessed.pack(pady=10)

        self.parts = [
            self.canvas.create_line(50, 150, 150, 150, state='hidden'),  # base
            self.canvas.create_line(100, 150, 100, 50, state='hidden'),  # vertical pole
            self.canvas.create_line(100, 50, 150, 50, state='hidden'),   # horizontal pole
            self.canvas.create_line(150, 50, 150, 70, state='hidden'),   # rope
            self.canvas.create_oval(140, 70, 160, 90, state='hidden'),   # head
            self.canvas.create_line(150, 90, 150, 120, state='hidden'),  # body
            self.canvas.create_line(150, 100, 140, 110, state='hidden'), # left arm
            self.canvas.create_line(150, 100, 160, 110, state='hidden'), # right arm
            self.canvas.create_line(150, 120, 140, 130, state='hidden'), # left leg
            self.canvas.create_line(150, 120, 160, 130, state='hidden')  # right leg
        ]

    def read(self, info):
        words = []
        with open(info, "r") as f:
            for line in f:
                words.append(line.strip().upper())
        return words

    def draw_hangman(self):
        if 10 - self.attempts < len(self.parts):  
            self.canvas.itemconfig(self.parts[10 - self.attempts], state='normal')

    def check_letter(self):
        guess = self.entry_letter.get().strip().upper()
        self.entry_letter.delete(0, tk.END)
        if not guess.isalpha():
            self.label_message.config(text="Solo puedes ingresar letras.")
            return
        if guess in self.guessed_letters:
            self.label_message.config(text="Ya has ingresado esa letra.")
            return
        self.guessed_letters.add(guess)
        self.label_guessed.config(text="Letras utilizadas: " + ", ".join(sorted(self.guessed_letters)))
        if guess in self.word_random:
            for idx in self.lyrics_dict[guess]:
                self.word_list_underscores[idx] = guess
            self.label_word.config(text=" ".join(self.word_list_underscores))
            if "_" not in self.word_list_underscores:
                self.label_message.config(text="Ganaste, la palabra era " + self.word_random)
                self.show_end_game_message("Ganaste")
        else:
            self.attempts -= 1
            self.label_message.config(text=f"Letra incorrecta. Intentos restantes: {self.attempts}")
            self.draw_hangman()
            if self.attempts == 0:
                self.label_message.config(text=f"Perdiste, la palabra era {self.word_random}")
                self.show_end_game_message("Perdiste")

    def show_end_game_message(self, result):
        for part in self.parts:
            self.canvas.itemconfig(part, state='normal')
        self.label_message.config(text=f"{result}, la palabra era {self.word_random}")
        self.entry_letter.config(state='disabled')
        self.button_check.config(state='disabled')
        self.button_play_again = tk.Button(self.master, text="Jugar de nuevo", command=self.reset_game)
        self.button_play_again.pack(pady=10)
        self.button_exit = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.button_exit.pack(pady=10)

    def reset_game(self):
        self.word_random = random.choice(self.word_list)
        self.word_list_underscores = ["_"] * len(self.word_random)
        self.lyrics_dict = {}
        for idx, letter in enumerate(self.word_random):
            if not self.lyrics_dict.get(letter):
                self.lyrics_dict[letter] = []
            self.lyrics_dict[letter].append(idx)
        self.attempts = 10  # Restablece los intentos a 10
        self.guessed_letters = set()
        self.label_word.config(text=" ".join(self.word_list_underscores))
        self.label_message.config(text="")
        self.label_guessed.config(text="Letras adivinadas: ")
        self.entry_letter.config(state='normal')
        self.button_check.config(state='normal')
        for part in self.parts:
            self.canvas.itemconfig(part, state='hidden')
        self.button_play_again.pack_forget()
        self.button_exit.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
