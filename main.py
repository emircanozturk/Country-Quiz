import random
import requests
import tkinter as tk
from PIL import Image, ImageTk

url = "https://restcountries.com/v3.1/all"

response = requests.get(url)
data = response.json()


def button_func():
    def create_index():
        return random.randint(0, 249)

    index = create_index()

    global data, var1, var2, var3, var4, var5, var6
    font = ("Bahnschrift", 22, "bold")
    for widget in frame5.winfo_children():
        widget.destroy()

    def country_name_func():
        if var1.get() == 1:
            c_name_data = data[index]["name"]["common"]
            c_name_label = tk.Label(frame5, text=f"Country Name: {c_name_data}", font=font)
            c_name_label.grid(sticky="w", pady=10, padx=10)

    def capital_name_func():
        if var2.get() == 1:
            try:
                capital_data = data[index]["capital"]
                for capital in capital_data:
                    capital_label = tk.Label(frame5, text=f"Capital/s: {capital}", font=font)
                    capital_label.grid(sticky="w", pady=8, padx=10)
            except:
                capital_label = tk.Label(frame5, text="Capital/s: ∅", font=font)
                capital_label.grid(sticky="w", pady=10, padx=10)

    def region_name_func():
        if var3.get() == 1:
            region_data = data[index]["region"]
            region_label = tk.Label(frame5, text=f"Region: {region_data}", font=font)
            region_label.grid(sticky="w", pady=10, padx=10)

    def flag_func():
        if var4.get() == 1:
            flag_img_pil = Image.open("flag.png")
            flag_img = ImageTk.PhotoImage(flag_img_pil)
            flag_label = tk.Label(frame5, image=flag_img)
            flag_label.image = flag_img
            flag_label.grid(column=1, row=0, padx=100)

    def language_func():
        try:
            if var5.get() == 1:
                language_data = data[index]["languages"]
                language_names = []

                for language in language_data:
                    if len(language_names) < 3:
                        language_names.append(language.upper())

                joined_names = ", ".join(language_names)
                language_label = tk.Label(frame5, text=f"Language/s: {joined_names}", font=font)
                language_label.grid(sticky="w", pady=10, padx=10)
        except:
            language_label = tk.Label(frame5, text="Language/s: ∅", font=font)
            language_label.grid(sticky="w", pady=10, padx=10)

    def population_func():
        if var6.get() == 1:
            population_data = data[index]["population"]
            population_label = tk.Label(frame5, text=f"Population: {population_data}", font=font)
            population_label.grid(sticky="w", pady=10, padx=10)

    country_name_func()
    capital_name_func()
    region_name_func()
    flag_func()
    language_func()
    population_func()


# UI
window = tk.Tk()
window.title("Country Quiz")
window.minsize(1024, 768)

frame1 = tk.Frame(window)
frame1.pack()
frame2 = tk.Frame(window)
frame2.pack()
frame3 = tk.Frame(window)
frame3.pack()
frame4 = tk.Frame(window)
frame4.pack()
frame5 = tk.Frame(window)
frame5.pack(anchor="w", pady=20)

img = ImageTk.PhotoImage(Image.open("logo.png"))
img_label = tk.Label(frame1, image=img)
img_label.pack(pady=10)

label = tk.Label(frame2, text="Choose below what you want to see about a random country.")
label.config(font=("Bahnschrift", 25, "bold"))
label.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

cbox_specs = [("country_name_cbox", "Country Name", var1),
              ("capital_name_cbox", "Capital", var2),
              ("region_name_cbox", "Region", var3),
              ("flag_cbox", "Flag", var4),
              ("language_cbox", "Language/s", var5),
              ("population_cbox", "Population", var6)
              ]

for code, name, variable in cbox_specs:
    cbox = tk.Checkbutton(frame3, text=name, font=("Bahnschrift", 15), variable=variable)
    cbox.update()
    cbox.pack(side="left", padx=32, pady=10)

randomize_img = tk.PhotoImage(file="randomize.png")
randomize_button = tk.Button(frame4, image=randomize_img, bd=4, command=button_func)
randomize_button.pack()

window.mainloop()

#uzun isim sorunları
#bayrak konumu sabit olmalı
