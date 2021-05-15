from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Weather app created by FelippoDev')
root.geometry("380x350")
myFont = font.Font(size=5)
my_canvas = Canvas(root, width=380, height=350)
my_canvas.grid(row=0, column=0)

bg = ImageTk.PhotoImage(Image.open('background.jpg'))
my_canvas.create_image(0, 0, image=bg, anchor=N + W)

my_canvas.create_text(160, 16, text='Check the wheather of your current location', font=('Helvetica'))


def get():
    city = city_entry.get()
    state = state_entry.get()
    api_request = requests.get(f"https://api.hgbrasil.com/weather?key=d08c55d1&amp;city_name={city},{state};locale=en")
    api = json.loads(api_request.content)

    temp_max = api['results']['forecast'][0]['max']
    temp_min = api['results']['forecast'][0]['min']
    description = api['results']['description']
    my_canvas.create_text(190, 310, text=f'Max temperature {temp_max}°C  Min temperature {temp_min}°C  {description}')


my_canvas.create_text(30, 80, text='City:', font=('Helvetica'))
city_entry = Entry(my_canvas, width=25, borderwidth=5)
my_canvas.create_window(120, 120, window=city_entry, height=32, width=200)

my_canvas.create_text(83, 180, text='State Abbreviation:', font=('Helvetica'))
state_entry = Entry(my_canvas, width=25, borderwidth=5)
my_canvas.create_window(120, 220, window=state_entry, height=32, width=200)

btn = Button(my_canvas, text='search', command=get)
btn.place(x=175, y=260)

root.mainloop()
