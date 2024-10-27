#Hangman game, consists of guessing letters, 
#until they can guess the word 
#complete before you run out of attempts

import tkinter as tk
import random
import platform
import os

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

        self.label_word = tk.Label(self.master, text=" ".join(self.word_list_underscores), font=('Helvetica', 18))
        self.label_word.pack(pady=20)
        self.entry_letter = tk.Entry(self.master, font=('Helvetica', 14))
        self.entry_letter.pack(pady=10)
        self.button_check = tk.Button(self.master, text="Probar", command=self.check_letter)
        self.button_check.pack(pady=10)
        self.label_message = tk.Label(self.master, text="", font=('Helvetica', 14))
        self.label_message.pack(pady=20)

    def read(self, info):
        words = []
        with open(info, "r") as f:
            for line in f:
                words.append(line.strip().upper())
        return words

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
        if guess in self.word_random:
            for idx in self.lyrics_dict[guess]:
                self.word_list_underscores[idx] = guess
            self.label_word.config(text=" ".join(self.word_list_underscores))
            if "_" not in self.word_list_underscores:
                self.label_message.config(text="Ganaste, la palabra era " + self.word_random)
                self.reset_game()
        else:
            self.attempts -= 1
            self.label_message.config(text=f"Letra incorrecta. Intentos restantes: {self.attempts}")
            if self.attempts == 0:
                self.label_message.config(text=f"Perdiste, la palabra era {self.word_random}")
                self.reset_game()

    def reset_game(self):
        self.word_random = random.choice(self.word_list)
        self.word_list_underscores = ["_"] * len(self.word_random)
        self.lyrics_dict = {}
        for idx, letter in enumerate(self.word_random):
            if not self.lyrics_dict.get(letter):
                self.lyrics_dict[letter] = []
            self.lyrics_dict[letter].append(idx)
        self.attempts = 10
        self.guessed_letters = set()
        self.label_word.config(text=" ".join(self.word_list_underscores))

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
