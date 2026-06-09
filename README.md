# App Clima

Aplicación de escritorio desarrollada en Python que permite consultar el clima actual de cualquier ciudad mediante una interfaz gráfica creada con Tkinter.

## Funcionalidades

- Consulta del clima por ciudad.
- Visualización de temperatura, sensación térmica, humedad, viento y presión.
- Manejo básico de errores de conexión y respuesta inesperada.
- Interfaz gráfica sencilla y limpia.

## Estructura del proyecto

```
app_clima/
├── src/
│   ├── app.py
│   ├── interface.py
│   └── weather_service.py
├── assets/
│   └── placeholder.txt
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Gutierrezor/app_clima.git
```

2. Entra al directorio e instala dependencias:

```bash
cd app_clima
pip install -r requirements.txt
```

3. Ejecuta la aplicación:

```bash
python src/app.py
```

## Vista previa

Agrega una captura de pantalla en `assets/app-clima-preview.png`. Hay un placeholder en `assets/placeholder.txt` con indicaciones.

## Notas

- Si deseas generar un ejecutable, instala `pyinstaller` y ejecuta:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed src/app.py
```

## Autor

Desarrollado por Julián Andrés Gutiérrez Ordoñez.
