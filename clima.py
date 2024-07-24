import requests
import tkinter as tk
from tkinter import messagebox

def obtener_clima(city):
    url = f"https://es.wttr.in/{city}?format=j1"
    
    response = requests.get(url)
    weather_dic = response.json()

    temp_c = weather_dic["current_condition"][0]['temp_C']
    desc_temp = weather_dic["current_condition"][0]['lang_es']
    desc_temp = desc_temp[0]['value']
    return temp_c, desc_temp

def mostrar_clima():
    ciudad = ciudad_entry.get()
    if ciudad:
        clima = obtener_clima(ciudad)
        messagebox.showinfo("Clima", clima)
    else:
        messagebox.showwarning("Por favor, ingrese una ciudad.")

app = tk.Tk()
app.title(" Clima ")

tk.Label(app, text="Ingrese la ciudad:").pack(pady=10)
ciudad_entry = tk.Entry(app)
ciudad_entry.pack(pady=5)

tk.Button(app, text="Obtener Clima", command=mostrar_clima).pack(pady=10)

app.mainloop()
