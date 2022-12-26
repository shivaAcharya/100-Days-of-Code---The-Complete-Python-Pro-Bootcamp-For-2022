from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# ################### DATA READING ####################

current_card = {}
data_dict = {}

try:
    df = pd.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"data\french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = df.to_dict(orient="records")


def get_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    random_idx = random.randint(0, len(data_dict) - 1)
    current_card = data_dict[random_idx]
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv(r"data\words_to_learn.csv", index=False)
    get_random_word()


def flip_card():
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)


# #################### UI SETUP ####################################

# Creating a new window and configurations
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Images
card_front_img = PhotoImage(file="images\\card_front.png")
card_back_img = PhotoImage(file="images\\card_back.png")
right_img = PhotoImage(file="images\\right.png")
wrong_img = PhotoImage(file="images\\wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=card_front_img)
title_txt = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Button
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=get_random_word)
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)

# Layout
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

get_random_word()
window.mainloop()
