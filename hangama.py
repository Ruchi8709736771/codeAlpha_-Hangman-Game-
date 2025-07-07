import tkinter as tk
from tkinter import messagebox
import random


words = ["apple", "banana", "cherry", "grape", "orange"]
secret_word = random.choice(words)
display = ['_' for _ in secret_word]
guessed_letters = []
wrong_guesses = 0
max_wrong = 6


def guess_letter():
    global wrong_guesses

    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        messagebox.showwarning("Invalid Input", "Enter a single alphabet letter.")
        return

    if letter in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{letter}'.")
        return

    guessed_letters.append(letter)

    if letter in secret_word:
        for idx, l in enumerate(secret_word):
            if l == letter:
                display[idx] = letter
        update_display()

        if '_' not in display:
            messagebox.showinfo("You Win!", f" Correct! The word was: {secret_word}")
            root.destroy()
    else:
        wrong_guesses += 1
        update_display()

        if wrong_guesses >= max_wrong:
            messagebox.showinfo("Game Over", f" You lost! The word was: {secret_word}")
            root.destroy()


def update_display():
    word_label.config(text=' '.join(display))
    guesses_label.config(text=f"Wrong Guesses: {wrong_guesses}/{max_wrong}")
    used_label.config(text=f"Guessed: {', '.join(guessed_letters)}")

# ----------------- GUI SETUP -----------------
root = tk.Tk()
root.title("Hangman Game - CodeAlpha")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="🎮 Hangman Game", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

word_label = tk.Label(root, text=' '.join(display), font=("Courier", 24))
word_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify='center')
entry.pack()

submit_btn = tk.Button(root, text="Guess", font=("Arial", 12), command=guess_letter)
submit_btn.pack(pady=10)

guesses_label = tk.Label(root, text=f"Wrong Guesses: {wrong_guesses}/{max_wrong}", font=("Arial", 12))
guesses_label.pack()

used_label = tk.Label(root, text="Guessed: None", font=("Arial", 12))
used_label.pack(pady=5)

root.mainloop()