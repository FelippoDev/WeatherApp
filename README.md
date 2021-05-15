# WeatherApp
Simple weather app using an API to get the weather data from an external database and using tkinter as GUI.

![ft (4)](https://user-images.githubusercontent.com/65267252/118350655-568aeb80-b52e-11eb-924a-a6e2e4e8e43b.png)




This is the start of the code where we setup the surface of the app.
```python
root = Tk()
root.title('Weather app created by FelippoDev')
root.geometry("380x350")
myFont = font.Font(size=5)
my_canvas = Canvas(root, width=380, height=350)
my_canvas.grid(row=0, column=0)


```

In this part of the code we set the layout of the buttons and the labels. 
```python

my_canvas.create_text(30, 80, text='City:', font=('Helvetica'))
city_entry = Entry(my_canvas, width=25, borderwidth=5)
my_canvas.create_window(120, 120, window=city_entry, height=32, width=200)

my_canvas.create_text(83, 180, text='State Abbreviation:', font=('Helvetica'))
state_entry = Entry(my_canvas, width=25, borderwidth=5)
my_canvas.create_window(120, 220, window=state_entry, height=32, width=200)

btn = Button(my_canvas, text='search', command=get)
btn.place(x=175, y=260)

```

The function `get` is the command that the button `btn` will receive every time is clicked.  
We use the `request` module to get the data from the database of the website using an API converting the data in JSON to Python language.

 ```python
def get():
    city = city_entry.get()
    state = state_entry.get()
    api_request = requests.get(f"https://api.hgbrasil.com/weather?key=d08c55d1&amp;city_name={city},{state};locale=en")
    api = json.loads(api_request.content)

    temp_max = api['results']['forecast'][0]['max']
    temp_min = api['results']['forecast'][0]['min']
    description = api['results']['description']
    my_canvas.create_text(190, 310, text=f'Max temperature {temp_max}°C  Min temperature {temp_min}°C  {description}')


```


## Contributors
@[FelippoDev](https://github.com/FelippoDev)
