# utils.py
import requests
from bs4 import BeautifulSoup
from flask import url_for

def extraer_informacion_enlace(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        titulo = soup.title.string if soup.title else "Sin título"
        descripcion = ""
        meta_descripcion = soup.find('meta', attrs={'name': 'description'})
        if meta_descripcion:
            descripcion = meta_descripcion.get('content', '')
        else:
            descripcion = "Descripción no disponible"

        imagen = ""
        meta_og_image = soup.find('meta', property='og:image')
        if meta_og_image:
            imagen = meta_og_image.get('content', '')
        else:
            imagen = url_for('static', filename='images/default_img.png')

        return titulo, descripcion, imagen

    except requests.exceptions.RequestException as e:
        print(f"Error al procesar el enlace: {e}")
        return "Error al extraer datos", "Descripción no disponible", url_for('static', filename='images/default_img.png')
