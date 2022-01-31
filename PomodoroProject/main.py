from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
REPS = 1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS

    if REPS % 2 == 1:
        timer_label.config(text="Work", font=("Comic Sans", 24, "bold"), fg=GREEN)
        countdown(1 * 60)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", font=("Comic Sans", 24, "bold"), fg=RED)
        countdown(1 * 60)
    elif REPS == 8:
        timer_label.config(text="Break", font=("Comic Sans", 24, "bold"), fg=RED)
        countdown(3 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global REPS
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    if count == 0:
        REPS += 1
        print(REPS)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Comic Sans", 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Click Start", font=("Comic Sans", 24, "bold"))
timer_label.config(bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=("Comic Sans", 12), highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", font=("Comic Sans", 12), highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_label = Label(text=CHECKMARK, font=("Comic Sans", 12))
check_label.config(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
