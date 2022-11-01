from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_lable.config(text="Timer")

    marks.config(text = "")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text = "Long break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lable.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)
        title_lable.config(text="Working", fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    import math
    count_minute = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        marks.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

title_lable = Label(text="Timer", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 30, "bold"))
title_lable.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer)

reset_button.grid(column=2, row=3)
marks = Label(fg=YELLOW, bg=GREEN, font=(FONT_NAME, 30))
marks.grid(column=1, row=4)
window.mainloop()
