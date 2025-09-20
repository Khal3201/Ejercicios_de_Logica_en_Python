'''
/*
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 */

'''
import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Hecho curioso sobre gatos:")
    print(data["fact"])
else:
    print("Error al conectar con la API.")

