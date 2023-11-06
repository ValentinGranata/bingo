from tkinter import *
from PIL import Image, ImageTk
import random

MAIN_COLOR = "#8d6955"
BG_COLOR = "#242424"
TEXT_COLOR = "#E7ECEF"
nums_to_extract = list(range(1, 91))


def extract_num():
    if len(nums_to_extract) == 0:
        return -1

    index = random.randint(0, len(nums_to_extract) - 1)
    num = nums_to_extract[index]
    del nums_to_extract[index]

    return num


# window
window = Tk()
window.iconbitmap('icon.ico')
window.geometry("900x550")
window.title("Tombola")
window.resizable(False, False)
window.config(padx=30, pady=30, bg=BG_COLOR)

# left
left = Frame(window, width=535, height=490)
left.propagate(False)
left.pack(side=LEFT)

circle_img_size = 48
circle_img = ImageTk.PhotoImage(Image.open("circle.png").resize((circle_img_size, circle_img_size)))
empty_img = ImageTk.PhotoImage(Image.open("empty.png").resize((circle_img_size, circle_img_size)))

table = [[None for x in range(10)] for y in range(9)]

i = 1

for y in range(0, 9):
    for x in range(0, 10):
        label = Label(left, text=i, width=circle_img_size, height=circle_img_size, image=empty_img, compound=CENTER, bg=BG_COLOR, fg=TEXT_COLOR, font=("Robot", 20, "bold"))
        label.grid(row=y, column=x)
        table[y][x] = label
        i += 1

# right
right = Frame(window, width=275, height=490, bg=BG_COLOR)
right.propagate(False)
right.pack(side=RIGHT)

# top
top = Frame(right, width=275, height=130, bg=BG_COLOR, pady=25)
top.propagate(False)
top.pack()

# title
title = Label(top, text="TOMBOLA", bg=BG_COLOR, fg=TEXT_COLOR)
title.config(font=("Roboto", 35, "bold"))
title.pack(fill=BOTH, expand=True)

# subtitle
subtitle = Label(top, text="IN CORSO...", bg=BG_COLOR, fg=MAIN_COLOR)
subtitle.config(font=("Roboto", 18))
subtitle.pack(fill=BOTH, expand=True)

# gap
gap = Frame(right, width=275, height=30, bg=BG_COLOR)
gap.pack()

# center
center = Frame(right, width=275, height=220, bg=BG_COLOR)
center.propagate(False)
center.pack()

# last number
table_img_size = 220
table_img = ImageTk.PhotoImage(Image.open("table.png").resize((table_img_size, table_img_size)))

last_extraction = Label(center, image=table_img, width=table_img_size, height=table_img_size, compound=CENTER, bg=BG_COLOR, fg=TEXT_COLOR, font=("Roboto", 60, "bold"))
last_extraction.grid(sticky="nsew")

# gap
gap = Frame(right, width=275, height=30, bg=BG_COLOR)
gap.pack()


# button
def calculate_table_index(num):
    res = int(num / 10)

    if num % 10 == 0:
        res -= 1

    return res, (num - res * 10) - 1


def on_click(event):
    num = extract_num()

    if num == -1:
        return

    pos = calculate_table_index(num)
    table[pos[0]][pos[1]]["image"] = circle_img
    table[pos[0]][pos[1]]["fg"] = MAIN_COLOR
    last_extraction["text"] = num

    if len(nums_to_extract) == 0:
        subtitle["text"] = "TERMINATA"
        button["fg"] = "gray"


button = Label(right, text="ESTRAI", width=275, height=80, font=("Roboto", 40, "bold"), bg=BG_COLOR, fg=TEXT_COLOR, cursor="heart", relief=SUNKEN)
button.bind("<Button-1>", on_click)
button.pack()

# refresh
window.mainloop()