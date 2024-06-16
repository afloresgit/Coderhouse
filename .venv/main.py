# import library OpenAI
from openai import OpenAI
# import API Key from sett.py
import sett

# configure API Key
client = OpenAI(api_key=sett.api_key)

# Funcion para crear el Itinerario del lugar a visitar
def generar_itinerario_viaje(lugar):
    # Crear un objeto para la solicitud de API
    # Llama a la API de OpenAI para generar itinerario en base al prompt
    prompt = f"Eres un agente de viajes de Chile. Debes proponer un itinerario de viaje para {lugar} que incluya recomendaciones de lugares y actividades para un día de estadía."
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        max_tokens=600, # Longitud maxima de la respuesta
        temperature=0,
        prompt = prompt
    ) 
    # Obtener la respuesta de la API
    itinerario = response.choices[0].text
    
    return itinerario

# Programa principal
if __name__ == "__main__":
    # Lugar a visitar
    lugar = input("Escriba el lugar que le gustaría visitar en Chile: ")
    print(f"Creando el itinerario de viaje para {lugar}...")
    # Generar itinerario
    itinerario = generar_itinerario_viaje(lugar)
    # Imprimir itinerario
    print(f"El itinerario de viaje para {lugar} es: {itinerario}")
    # Guardar itinerario en un archivo de texto
    with open(f"{lugar}_itinerario.txt", "w") as f:
        f.write(itinerario)
    
