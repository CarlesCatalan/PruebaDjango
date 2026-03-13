import requests
from django.shortcuts import render

from PruebaDjango.settings import OPENWEATHER_API_KEY


def clima(request):
    ciudad = 'Palma'
    api_key = OPENWEATHER_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            clima_info = {
                'ciudad': ciudad,
                'temperatura': data['main']['temp'],
                'descripcion': data['weather'][0]['description'],
                'icono': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
            }
            return render(request, 'clima/clima.html', {'clima': clima_info})
        else:
            error = f"Error al obtener datos del clima: {response.status_code}"
            return render(request, 'clima/clima.html', {'error': error})
    except requests.exceptions.RequestException as e:
        error = f"Error de conexión: {e}"
        return render(request, 'clima/clima.html', {'error': error})
