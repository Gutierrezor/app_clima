import tkinter as tk
from tkinter import messagebox

from weather_service import obtener_clima


def main():
    app = tk.Tk()
    app.title("App Clima")
    app.geometry("420x320")
    app.configure(bg="#EAF4F4")
    app.resizable(False, False)

    titulo = tk.Label(
        app,
        text="Consulta del Clima",
        font=("Arial", 16, "bold"),
        bg="#EAF4F4",
    )
    titulo.pack(pady=12)

    frame = tk.Frame(app, bg="#EAF4F4")
    frame.pack(pady=6)

    tk.Label(frame, text="Ciudad:", bg="#EAF4F4").grid(row=0, column=0, sticky="e", padx=5)
    ciudad_entry = tk.Entry(frame, width=30)
    ciudad_entry.grid(row=0, column=1, padx=5)

    resultado = tk.Label(
        app,
        text="",
        bg="#FFFFFF",
        width=50,
        height=8,
        anchor="nw",
        justify="left",
        bd=1,
        relief="solid",
    )
    resultado.pack(pady=10)

    def limpiar():
        ciudad_entry.delete(0, tk.END)
        resultado.config(text="")

    def mostrar():
        ciudad = ciudad_entry.get().strip()
        if not ciudad:
            messagebox.showwarning("Campo vacío", "Por favor, ingrese una ciudad.")
            return
        try:
            datos = obtener_clima(ciudad)
            texto = (
                f"Ciudad: {ciudad}\n"
                f"Temperatura: {datos.get('temperatura')}°C\n"
                f"Sensación: {datos.get('sensacion')}°C\n"
                f"Descripción: {datos.get('descripcion')}\n"
                f"Humedad: {datos.get('humedad')}%\n"
                f"Viento: {datos.get('viento')} km/h\n"
                f"Presión: {datos.get('presion')} hPa"
            )
            resultado.config(text=texto)
        except Exception as exc:
            messagebox.showerror("Error", f"No se pudo obtener la información del clima.\n{exc}")

    botones = tk.Frame(app, bg="#EAF4F4")
    botones.pack(pady=6)
    tk.Button(botones, text="Obtener clima", command=mostrar).grid(row=0, column=0, padx=6)
    tk.Button(botones, text="Limpiar", command=limpiar).grid(row=0, column=1, padx=6)
    tk.Button(botones, text="Salir", command=app.quit).grid(row=0, column=2, padx=6)

    app.mainloop()
