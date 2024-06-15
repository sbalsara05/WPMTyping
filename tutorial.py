import tkinter as tk
import time
import threading
import random


class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed")
        self.root.geometry("800x600")

        self.text = open("texts.txt", "r").read().split("\n")

        self.sample_label = tk.Label(self.root, text=random.choice(self.text), font=("Helvetica", 20))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.root, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        self.speed_label = tk.Label(self.root, text="Speed: \n0.00 Characters per Second\n0.00 Characters per Minute", font=("Helvetica", 14))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(text="Reset Button", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
