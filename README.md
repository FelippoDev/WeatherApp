# WeatherApp
Simple weather app using an API to get the weather data from an external database and using tkinter as GUI for receiving the input.

![ft (4)](https://user-images.githubusercontent.com/65267252/118350655-568aeb80-b52e-11eb-924a-a6e2e4e8e43b.png)




This is the start of the code where we setup the surface of the app.
```python
root = Tk()
root.title('Weather app created by FelippoDev')
root.geometry("550x120")

head = Label(root, text='Check the wheather of your current location', font=("Helvetica"))
head.grid(row=0, column=0)

```

In this part of the code we set the layout of the buttons and the labels. 
```python

city_label = Label(root, text='City', font=('Helvetica'))
city_label.grid(row=1, column=0)

state_label = Label(root, text='State Abbreviation', font=('Helvetica'))
state_label.grid(row=2, column=0)

city_entry = Entry(root, width=25, borderwidth=5)
city_entry.grid(row=1, column=1)

state_entry = Entry(root, width=25, borderwidth=5)
state_entry.grid(row=2, column=1)

btn = Button(root, text='search', command=get)
btn.grid(row=3, column=1)

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
    label = Label(root, text=f'Max temperature {temp_max}°C  Min temperature {temp_min}°C  {description}')
    label.grid(row=3, column=0)

```


## Contributors
@[FelippoDev](https://github.com/FelippoDev)
