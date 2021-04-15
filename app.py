from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Weather app created by FelippoDev')
root.geometry("550x120")

head = Label(root, text='Check the wheather of your current location', font=("Helvetica"))
head.grid(row=0, column=0)


def get():
    city = city_entry.get()
    state = state_entry.get()
    api_request = requests.get(f"https://api.hgbrasil.com/weather?key=d08c55d1&amp;city_name={city},{state};locale=en")
    api = json.loads(api_request.content)

    temp_max = api['results']['forecast'][0]['max']
    temp_min = api['results']['forecast'][0]['min']
    description = api['results']['description']
    label = Label(root, text=f'Max temperature {temp_max}°C  Min temperature {temp_min}°C  {description}')
    label.grid(row=3, column=0)


city_label = Label(root, text='City', font=('Helvetica'))
city_label.grid(row=1, column=0)

state_label = Label(root, text='State Abb', font=('Helvetica'))
state_label.grid(row=2, column=0)

city_entry = Entry(root, width=25, borderwidth=5)
city_entry.grid(row=1, column=1)

state_entry = Entry(root, width=25, borderwidth=5)
state_entry.grid(row=2, column=1)

btn = Button(root, text='search', command=get)
btn.grid(row=3, column=1)

root.mainloop()
