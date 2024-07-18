from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = []

# Read data from CSV
try:
    data = pd.read_csv(r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Flash Card Project\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Flash Card Project\data\french_words.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")

# Function to show the next card
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)  # Pick a random card
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(front, image=card_front)
    flip_timer = window.after(3000, flip_card)

# Function to flip the card
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(front, image=card_back)

# Function to remove the known card
def known():
    global learn
    learn.remove(current_card)
    data = pd.DataFrame(learn)
    data.to_csv(r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Flash Card Project\data\words_to_learn.csv", index=False)
    next_card()

# Set up the window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

# Load images
card_front = PhotoImage(file=r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Flash Card Project\Images\card_front.png")
card_back = PhotoImage(file=r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Flash Card Project\Images\card_back.png")
wrong = PhotoImage(file=r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Flash Card Project\Images\wrong.png")
right = PhotoImage(file=r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Flash Card Project\Images\right.png")

# Set up the canvas
canvas = Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
front = canvas.create_image(400, 268, image=card_front)
canvas.grid(column=0, row=1, columnspan=2)

# Text on the card
card_title = canvas.create_text(400, 115, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Buttons
button1 = Button(image=wrong, highlightthickness=0, command=next_card)
button1.grid(column=0, row=2)

button2 = Button(image=right, highlightthickness=0, command=known)
button2.grid(column=1, row=2)

# Start the first card
next_card()

# Main loop
window.mainloop()
