BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random


##read data
random_word_pair = {}
data_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    print("File not Found")
    data = pd.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    print("read from words to learn")
    data_dict = data.to_dict(orient = "records")



def choose_random_french_word():
    global random_word_pair, flip_timer
    window.after_cancel(flip_timer)
    random_word_pair = random.choice(data_dict)
    canvas.itemconfig(title_text, text= "French", fill = "black")
    canvas.itemconfig(word_text,text = random_word_pair["French"], fill = "black")
    canvas.itemconfig(canvas_img, image = front_img)
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word_pair["English"], fill="white")
    canvas.itemconfig(canvas_img, image=back_img)


def remove_from_list():
    data_dict.remove(random_word_pair)
    new_data = pd.DataFrame.from_dict(data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)


##Create UI
# Setup window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)

# Setup canvas
card_front_img_name = "images/card_front.png"
card_back_img_name = "images/card_back.png"
front_img = PhotoImage(file = card_front_img_name)
back_img = PhotoImage(file = card_back_img_name)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400,263,image = front_img)
title_text = canvas.create_text(400,150,text = "Title", font = ("Ariel",40, "italic"))
word_text = canvas.create_text(400,263,text = "Word", font = ("Ariel",60, "bold"))
canvas.grid(column = 0,row = 0, columnspan =2)

#Settup buttons
corr_img_name = "images/right.png"
corr_img = PhotoImage(file = corr_img_name)

wrong_img_name = "images/wrong.png"
wrong_img = PhotoImage(file = wrong_img_name)

correct_button = Button(image=corr_img, padx = 50, pady =50, highlightthickness=0, command=lambda:[choose_random_french_word(), remove_from_list()])
correct_button.grid(column = 0, row = 1)

wrong_button = Button(image=wrong_img, padx = 50, pady =50, highlightthickness=0,command = choose_random_french_word)
wrong_button.grid(column = 1, row = 1)

window.mainloop()