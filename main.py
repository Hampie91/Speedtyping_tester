import random
from tkinter import *
import datetime as dt

window = Tk()
window.geometry("900x600")
window.config(bg="#d8e3e7")
window.title("Speedtyping tester")

NORMAL_TEXT_FONT = ("arial", 11, "normal")

WORDS_TYPED = 0
CHARACTERS_TYPED= 0
TIME = 60 #seconds


#Getting the dutch words out of the txt file and saving them in a list.
with open("dutch_words.txt") as words:
    dutch_words = words.readlines()

dutch_word_list = []
for word in dutch_words:
    new_word = word.split('\n')[0].lower()
    dutch_word_list.append(new_word)

#---------------------------------------Code----------------------------------------------------#

#getting random words out of the word list and adding them to a new list.
shown_word_list = []
if len(shown_word_list) < 15:
    for item in range(15):
        random_word = random.choice(dutch_word_list)
        shown_word_list.append(random_word)


def start_timer(event=None):
    window.unbind("<Key>")
    count_down(TIME)


def count_down(time):
    if time > 0:
        time_counter.config(text=time)
        timer = window.after(1000, count_down, time - 1)
    if time == 0:
        time_counter.config(text=time)
        cpm_label.config(text=f"Your CPM is: {CHARACTERS_TYPED / (TIME / 60)}")
        wpm_label.config(text=f"Your WPM is: {WORDS_TYPED / (TIME / 60)}") #This way because I can change the time without breaking score
        safe_score()

def safe_score():
    with open("score_file.txt", "a") as file:
        file.write(f"{dt.datetime.now()}CPM:{CHARACTERS_TYPED / (TIME / 60)} WPM:{WORDS_TYPED / (TIME / 60)}\n")

def update_list(event=None):
    global shown_word_list
    global WORDS_TYPED
    global CHARACTERS_TYPED
    entered_word = str(typing_field.get().rstrip())
    check_word = str(shown_word_list[0])
    if entered_word == check_word:
        WORDS_TYPED +=1
        CHARACTERS_TYPED += len(check_word)
        word_list_label.config(bg="#81ff7d") #change the color based on correct last word.
    else:
        word_list_label.config(bg="#f78d8d") #change the color based on last word.

    typing_field.delete(0, "end")
    shown_word_list.append(pick_random_word())
    print(WORDS_TYPED, CHARACTERS_TYPED)
    shown_word_list.pop(0)
    word_list_label.config(text=f"{shown_word_list[0]} {shown_word_list[1]} {shown_word_list[2]} {shown_word_list[3]} {shown_word_list[4]}\n"
                             f"{shown_word_list[5]} {shown_word_list[6]} {shown_word_list[7]} {shown_word_list[8]} {shown_word_list[9]}\n"
                             f"{shown_word_list[10]} {shown_word_list[11]} {shown_word_list[12]} {shown_word_list[13]} {shown_word_list[14]}")



def pick_random_word():
    random_word = random.choice(dutch_word_list)
    return random_word
#---------------------------------------Interface----------------------------------------------------#


#labels

cpm_label = Label(text=f"Your CPM is: {0}",
                  font=NORMAL_TEXT_FONT, bg="#51c4d3")
cpm_label.place(x=50, y=10)

wpm_label = Label(text=f"Your WPM is: {0}",
                  font=NORMAL_TEXT_FONT, bg="#51c4d3")
wpm_label.place(x=400, y=10)

time_left_label = Label(text="Time left:",
                        font=NORMAL_TEXT_FONT, bg="#51c4d3")
time_left_label.place(x=750, y=10)

time_counter = Label(text=TIME, font=NORMAL_TEXT_FONT, bg="#51c4d3")
time_counter.place(x=815, y=10)

word_list_label = Label(text=f"{shown_word_list[0]} {shown_word_list[1]} {shown_word_list[2]} {shown_word_list[3]} {shown_word_list[4]}\n"
                             f"{shown_word_list[5]} {shown_word_list[6]} {shown_word_list[7]} {shown_word_list[8]} {shown_word_list[9]}\n"
                             f"{shown_word_list[10]} {shown_word_list[11]} {shown_word_list[12]} {shown_word_list[13]} {shown_word_list[14]}",
                        font=("arial", 20, "normal"), relief=SUNKEN, width=45)
word_list_label.place(x=95, y=100)

#Entry field
typing_field = Entry(width=20, font=("arial", 16, "normal"), justify="center", bd=2)
typing_field.place(x=340, y=250)



window.bind("<space>", update_list)


window.bind("<Key>", start_timer)

window.mainloop()