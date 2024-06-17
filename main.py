from tkinter import *
from content import Content

# width and height of window
WIDTH = 1500
HEIGHT = 700

timer = 60
# using font
FONT = ("Arial", 22)
FONT2 = ("Courier", 22, "bold")
FONT3 = ("Courier", 32, "bold")

# content to show on test box
post = Content()

content = post.get_content()

comparing_content: list = content.split(" ")

# word position
current_index = 0
cursor = 0

score = 0

# color
TEXT_BOX = "#F1F8E8"
BG_COLOR = "#D8EFD3"

# window
window = Tk()


def highlight(word, is_correct):
    """ highlighting correct and wrong word with colors"""
    global cursor

    # Find the start and end positions of the word
    start_pos = cursor

    end_pos = start_pos + len(word)
    start_index = f"1.0 + {start_pos} chars"
    end_index = f"1.0 + {end_pos} chars"

    if is_correct:
        text_box.tag_add('correct', start_index, end_index)
    else:
        text_box.tag_add('incorrect', start_index, end_index)

    if is_correct:
        text_box.tag_configure('correct', background='green', foreground='white')

    else:
        text_box.tag_configure('incorrect', background='red', foreground='white')

    cursor += len(word) + 1


def countdown(count):
    if count >= 0:
        time_text["text"] = f"Time left:- {count}"
        window.after(1000, countdown, count - 1)
    else:
        text_box.place_forget()
        entry.place_forget()
        result["text"] = f"your score is {score} WPM"
        result.pack(expand=True)
        restart_button.pack(expand=True)


def moniter(event):
    # monitoring
    global current_index, score, cursor
    # fetching user input
    user_input: str = entry.get()
    entry.delete(0, END)
    if current_index >= len(comparing_content) - 1:
        print("done")
        typer(True)
        current_index = 0
        cursor = 0
        return 0
    # grabing content current word
    correct = comparing_content[current_index]

    if len(user_input) >= len(correct):
        # cleaned word with white-spaces
        clean = user_input.strip()

        if clean == correct:
            score += 1
            highlight(correct, True)
            # print("correct:-", score)
        else:
            highlight(correct, False)

    else:
        highlight(correct, False)

    current_index += 1


def start():
    start_button.pack_forget()
    head.pack_forget()
    countdown(timer)
    typer()


def restart():
    global score, current_index, cursor
    entry.delete(0, END)
    text_box.tag_remove('correct', '1.0', END)
    text_box.tag_remove('incorrect', '1.0', END)
    result.pack_forget()
    restart_button.pack_forget()
    score = 0
    current_index = 0
    cursor = 0
    countdown(timer)
    typer(True)


def typer(is_restart=False):
    global comparing_content, content
    # timer position
    time_text.place(relx=0.8, rely=0.01)
    # text_box position
    text_box.place(relx=0.25, rely=0.1)

    # deleting the content in of text box
    text_box.delete("1.0", END)

    # repopulating the content
    if is_restart:
        content = post.get_content()
        comparing_content = content.split(" ")
    text_box.insert(END, content)


    # entry position
    entry.place(relx=0.4, rely=0.6)
    entry.bind("<Return>", moniter)
    entry.focus_set()


# ________main code _______

window.title("Typing Master")
window.minsize(WIDTH, HEIGHT)
window.config(background=BG_COLOR,
              pady=10)
# Heading
head = Label(text="Typer Faster", font=("Serif",100,"italic bold"),foreground='brown', background=BG_COLOR)
head.pack(expand=True)
# start button
start_button = Button(text="Start", font=FONT2, command=start)
start_button.pack(expand=True)

# score board
result = Label(font=FONT3, foreground="grey", padx=10)

# restart button
restart_button = Button(text="Restart", font=FONT2, command=restart)

time_text = Label(text="Time left:- 60", font=("Arial", 22, "bold"), foreground="grey", background=BG_COLOR)

text_box = Text(window,
                background=TEXT_BOX,
                borderwidth=4,
                font=FONT,
                height=10,
                width=50,
                padx=2,
                pady=2
                )

entry = Entry(window)

entry.config(width=15,
             font=FONT,
             )

window.mainloop()
