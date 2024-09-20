from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
current_session = 0  # immutable
timer = ""


def update_session(session):
    return session + 1


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    master.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")  # padding with zeros
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    start_button['state'] = NORMAL
    global current_session
    current_session = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Count the time in seconds since we click the "start" button
    :return: None
    """

    global current_session
    current_session += 1
    start_button["state"] = DISABLED

    if current_session % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)  # long break

    elif current_session % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)  # short break
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)  # work


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):  # recursive function
    """
    accept count in seconds and convert it to minutes + calculate the remainder in seconds.
    :param count: seconds
    :return: None
    """
    count_min = count // 60  # work/break time in minutes
    count_sec = count % 60  # remainder in seconds

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")  # padding with zeros

    if count > 0:
        global timer
        timer = master.after(1000, count_down, count - 1)  # method of Misk Class - every second
    else:  # session end
        start_timer()
        work_session_num = current_session // 2
        checkmark_label.config(text="🗸" * work_session_num)


# ---------------------------- UI SETUP ------------------------------- #

master = Tk()  # Tk object
master.title("Pomodoro")
master.config(padx=100, pady=60, bg=YELLOW)  # Tk class method

# Canvas object
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# PhotoImage object
tomato_img = PhotoImage(file="tomato.png")

# Canvas class methods:
canvas.create_image(100, 112, image=tomato_img)  # create image item --> return Int object
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # text item (int)
canvas.grid(row=1, column=1)

# Label objects:
timer_label = Label(master, text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

checkmark_label = Label(master, font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

# button objects:
start_button = Button(master, text="Start", font=("Ariel", 14, "bold"), fg="blue", bg="lime", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(master, text="Reset", font=("Ariel", 14, "bold"), fg="blue", bg="silver", command=reset_timer)
reset_button.grid(row=2, column=2)

# looping through and every millisecond it's checking to see if something happen
master.mainloop()
