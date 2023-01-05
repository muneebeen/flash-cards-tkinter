from tkinter import *
import pandas
import random
import os

TIMER = None
BACKGROUND_COLOR = "#B1DDC6"

# Read CSV
if os.path.exists('./data/Words_to_learn.csv'):
    data = pandas.read_csv("./data/Words_to_learn.csv")
    print("Getting words from words to learn file.")
else:
    data = pandas.read_csv("./data/french_words.csv")
    print("Getting words from french_words file.")
words_list = data.to_dict(orient="records")
current_word = {}


# change words
def change_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_list)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_word['French'], fill="black")
    canvas.itemconfig(card, image=card_front_photo)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_word['English'], fill="white")
    canvas.itemconfig(card, image=card_back_photo)


def is_known():
    words_list.remove(current_word)
    updated_data = pandas.DataFrame(words_list)
    updated_data.to_csv("./data/Words_to_learn.csv", index=False)
    change_word()

# UI
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_photo = PhotoImage(file="./images/card_front.png")
card_back_photo = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_photo)
title = canvas.create_text(400, 150, text="", fill="black", font=('Arial', 20, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=('Arial', 30, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, pady=50)

wrong_photo = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_photo, highlightthickness=0, command=change_word)
wrong_btn.grid(row=1, column=0)


right_photo = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_photo, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)


change_word()

window.mainloop()




