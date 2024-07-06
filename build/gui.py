
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#importing other files
import main


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abdur\OneDrive\Desktop\housing-ml\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1080x720")
window.configure(bg = "#273F43")


canvas = Canvas(
    window,
    bg = "#273F43",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    300.0,
    100.0,
    anchor="nw",
    text="House price AI",
    fill="#FFFFFF",
    font=("Inter", 72 * -1)
)

canvas.create_rectangle(
    196.0,
    222.0,
    884.0,
    674.0,
    fill="#161B22",
    outline="")

canvas.create_text(
    263.0,
    264.0,
    anchor="nw",
    text="Rooms",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)


rooms = entry_1.get()
baths = entry_2.get()
land = entry_3.get()
lat = entry_4.get()
lon = entry_5.get()


def valid_rooms():
    try:
        float(rooms)
        entry_1.config(
            fg= '#FFFFFF'
        )
        rooms = float(rooms)
        return True
    except ValueError:
        return False
    
def invalid_rooms():
    entry_1.config(
        fg= 'red'
    )

def valid_bath():
    try:
        float(baths)
        entry_2.config(
            fg= '#FFFFFF'
        )
        baths = float(baths)
        return True
    except ValueError:
        return False

def invalid_bath():
    entry_2.config(
        fg= 'red'
    )

def valid_land():
    try:
        float(land)
        entry_3.config(
            fg= '#FFFFFF'
        )
        land = float(land)
        return True
    except ValueError:
        return False
    
def invalid_land():
    entry_3.config(
        fg= 'red'
    )

def valid_lat():
    try:
        float(lat)
        entry_4.config(
            fg= '#FFFFFF'
        )
        lat = float(lat)
        return True
    except ValueError:
        return False
    
def invalid_lat():
    entry_4.config(
        fg= 'red'
    )

def valid_lon():
    try:
        float(lon)
        entry_5.config(
            fg= '#FFFFFF'
        )
        lon = float(lon)
        return True
    except ValueError:
        return False

def invalid_lon():
    entry_5.config(
        fg= 'red'
    )

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    642.5,
    278.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#273F43",
    fg="#FFFFFF",
    font="Helvetica",
    justify="left",
    highlightthickness=0,
    validatecommand=valid_rooms,
    validate="focusout",
    invalidcommand=invalid_rooms
)
entry_1.place(
    x=435.0,
    y=263.0,
    width=415.0,
    height=29.0
)

canvas.create_text(
    230.0,
    548.0,
    anchor="nw",
    text="Longitude",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    642.5,
    569.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#273F43",
    fg="#FFFFFF",
    font="Helvetica",
    justify="left",
    highlightthickness=0,
    validatecommand=valid_lon,
    validate='focusout',
    invalidcommand=invalid_lon
)
entry_5.place(
    x=435.0,
    y=554.0,
    width=415.0,
    height=29.0
)

canvas.create_text(
    272.0,
    336.0,
    anchor="nw",
    text="Baths",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    642.5,
    351.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#273F43",
    fg="#FFFFFF",
    font="Helvetica",
    justify="left",
    highlightthickness=0,
    validatecommand=valid_bath,
    validate='focusout',
    invalidcommand=invalid_bath
)
entry_2.place(
    x=435.0,
    y=336.0,
    width=415.0,
    height=29.0
)

canvas.create_text(
    252.0,
    402.0,
    anchor="nw",
    text="Landsize",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    642.5,
    423.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#273F43",
    fg="#FFFFFF",
    font="Helvetica",
    justify="left",
    highlightthickness=0,
    validatecommand=valid_land,
    validate='focusout',
    invalidcommand=invalid_land
)
entry_3.place(
    x=435.0,
    y=408.0,
    width=415.0,
    height=29.0
)

canvas.create_text(
    252.0,
    476.0,
    anchor="nw",
    text="Latitude",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    642.5,
    497.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#273F43",
    fg="#FFFFFF",
    font="Helvetica",
    justify="left",
    highlightthickness=0,
    validatecommand=valid_lat,
    validate='focusout',
    invalidcommand=invalid_lat
)
entry_4.place(
    x=435.0,
    y=482.0,
    width=415.0,
    height=29.0
)


def valid_all():
    if valid_rooms() and valid_bath() and valid_land() and valid_lat() and valid_lon():
        
        # prediction
        def predict():

            pred = main.predict(rooms, baths, land, lat, lon)
            return pred

        # show new screen
        from new.result import new_screen
        new_screen(predict, window)

    else:
        print('Invalid values')



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [valid_all()],
    relief="flat"
)
button_1.place(
    x=420.0,
    y=603.0,
    width=248.0000157356244,
    height=61.000003993510745
)


window.resizable(True, True)
window.mainloop()
