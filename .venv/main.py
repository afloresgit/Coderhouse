# import library OpenAI
from openai import OpenAI
# import API Key from sett.py
import sett
# import Streamlit
import streamlit as st

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

# Funciones para adecuar Streamlit

def main():
    st.title('Itinerarios para viajes')

    st.sidebar.title('Menú')
    app_mode = st.sidebar.selectbox('Elige una opción', ['Ayuda', 'Inicio'])

    if app_mode == 'Inicio':
        run_app()
    elif app_mode == 'Ayuda':
        show_help()

def run_app():
    #st.header('Inicio')
    # Lugar a visitar
    lugar = st.text_input("Escriba el lugar que le gustaría visitar en Chile y presione el botón Generar: ")
    if st.button('Generar'):
        with st.spinner("Creando el itinerario de viaje para " + lugar + "..."):
            # Generar itinerario
            itinerario = generar_itinerario_viaje(lugar)
            # Imprimir itinerario
            st.write(f"El itinerario de viaje para {lugar} es: {itinerario}")
            # Guardar itinerario en un archivo de texto
            with open(f"{lugar}_itinerario.txt", "w") as f:
                f.write(itinerario)
            #st.write(f"El itinerario fue grabado en archivo: {lugar}_itinerario.txt")
            st.success("Itinerario generado")

def show_help():
    st.header('Ayuda')
    st.write('''
    Aquí puedes encontrar ayuda sobre cómo operar la aplicación:

    1. Ve al menú en la barra lateral izquierda.
    2. Elige la opción 'Inicio' para introducir información.
    3. Escribe tu consulta en el cuadro de texto.
    4. Haz clic en el botón 'Enviar' para visualizar la respuesta.
    ''')

# Programa principal
if __name__ == "__main__":
    main()
    
