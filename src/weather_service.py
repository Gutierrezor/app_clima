import requests


def obtener_clima(ciudad: str) -> dict:
    """Consulta wttr.in y devuelve un diccionario con valores relevantes.

    Lanza `requests.exceptions.RequestException` si hay error de conexión
    o `ValueError`/`KeyError` si la respuesta no tiene el formato esperado.
    """
    url = f"https://es.wttr.in/{ciudad}?format=j1"

    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    datos = resp.json()

    try:
        current = datos["current_condition"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise KeyError("Respuesta inesperada de la API") from exc

    temperatura = current.get("temp_C")
    sensacion = current.get("FeelsLikeC")
    humedad = current.get("humidity")
    viento = current.get("windspeedKmph")
    presion = current.get("pressure")

    descripcion = None
    if isinstance(current.get("lang_es"), list) and current.get("lang_es"):
        descripcion = current["lang_es"][0].get("value")
    else:
        descripcion = (current.get("weatherDesc") or [{}])[0].get("value")

    return {
        "temperatura": temperatura,
        "sensacion": sensacion,
        "humedad": humedad,
        "viento": viento,
        "presion": presion,
        "descripcion": descripcion,
        "raw": datos,
    }
